import numpy as np
import pandas as pd
import pymssql
from flask import Flask, request, render_template
from sklearn.preprocessing import MinMaxScaler 
from feature_engineering import *
import pickle
import warnings

warnings.filterwarnings('ignore')

model = pickle.load(open('DAE_PatientsSatisfaction.pkl', 'rb'))

app = Flask(__name__, template_folder='templates')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['GET','POST'] )

def predict():
    conn = pymssql.connect(server='103.13.96.124', user='ReadonlyAll', password='abcd0123!', database='PXPFassco')
    cursor = conn.cursor(as_dict=True)
    form_date = pd.to_datetime(request.form.get('date')).strftime('%Y-%m-%d')
    cursor.callproc('dbo.sp_rd_ML_DAE_EVS_Cleaningness', (form_date,))
    rows = []
    for row in cursor:
        rows.append(row)
    df1 = pd.DataFrame(rows)
    cursor.close()
    conn.close()    
    
    df1['PatientRoomInspection'] = df1[['PatientRoomInspection','StaircaseInspection']].apply(impute_PatientRoomInspection,axis=1)
    df1['OfficeInspection'] = df1[['OfficeInspection','PublicAreaRestRoomInspection']].apply(impute_OfficeInspection,axis=1)
    df1['WaitingAreaInspection'] = df1[['WaitingAreaInspection','SoiledUtilityInspection']].apply(impute_WaitingAreaInspection,axis=1)
    df1['LiftBankInspection'] = df1[['LiftBankInspection','EntranceInspection']].apply(impute_LiftBankInspection,axis=1)
    df1['StaircaseInspection'] = df1[['StaircaseInspection','LiftBankInspection']].apply(impute_StaircaseInspection,axis=1)
    df1['MedicalWasteRoomInspection'] = df1[['MedicalWasteRoomInspection','HousekeepingClosetInspection']].apply(impute_MedicalWasteRoomInspection,axis=1)
    df1['PublicAreaRestRoomInspection'] = df1[['PublicAreaRestRoomInspection','StaircaseInspection']].apply(impute_PublicAreaRestRoomInspection,axis=1)
    df1['HousekeepingClosetInspection'] = df1[['HousekeepingClosetInspection','StaircaseInspection']].apply(impute_HousekeepingClosetInspection,axis=1)
    df1['SoiledUtilityInspection'] = df1[['SoiledUtilityInspection','PublicAreaRestRoomInspection']].apply(impute_SoiledUtilityInspection,axis=1)
    df1['HousekeepingCartInspection'] = df1[['HousekeepingCartInspection','OfficeInspection']].apply(impute_HousekeepingCartInspection,axis=1)
    df1['CorridorsAndHallwayInspection'] = df1[['CorridorsAndHallwayInspection','EntranceInspection']].apply(impute_CorridorsAndHallwayInspection,axis=1)
    df1['EntranceInspection'] = df1[['EntranceInspection','LiftBankInspection']].apply(impute_EntranceInspection,axis=1)
    df1 = df1[['PatientRoomInspection','OfficeInspection','WaitingAreaInspection','LiftBankInspection','StaircaseInspection','MedicalWasteRoomInspection','PublicAreaRestRoomInspection','HousekeepingClosetInspection','SoiledUtilityInspection','HousekeepingCartInspection','CorridorsAndHallwayInspection','EntranceInspection']].copy()
    print(df1.values)
    scaler = MinMaxScaler()
    x = df1.values
    x_scaled = scaler.fit_transform(x)
    x = pd.DataFrame(x_scaled)
    feature_list = x.values[0].tolist()
    final_features = np.array(feature_list).reshape(1, 12)
    prediction = model.predict(final_features)
    
    def statement():
        output = int(prediction[0])
        if output == 1:
            return "Good"
        elif output == 2:
            return "Very Good"
        else:
            return str(output)
    return render_template('index.html',statement='Patients Satisfaction is "{}" for the date, {}.'.format(statement(),form_date))

if __name__=='__main__':
    app.debug = True
    app.run()