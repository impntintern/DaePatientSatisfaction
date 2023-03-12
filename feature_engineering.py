import pandas as pd

def impute_PatientRoomInspection(cols):
    PatientRoomInspection = cols[0]
    StaircaseInspection = cols[1]    
    if pd.isnull(PatientRoomInspection):
        if StaircaseInspection == -1:
            return 15
        elif StaircaseInspection == 0:
            return 15
        elif StaircaseInspection == 1:
            return 15
        elif StaircaseInspection == 2:
            return 15
        elif StaircaseInspection == 3:
            return 22
        elif StaircaseInspection == 4:
            return 17
        elif StaircaseInspection == 5:
            return 21.5
        elif StaircaseInspection == 6:
            return 21
        elif StaircaseInspection == 7:
            return 21.5
        elif StaircaseInspection == 8:
            return 25
        elif StaircaseInspection == 9:
            return 25
        elif StaircaseInspection == 10:
            return 26
        elif StaircaseInspection == 11:
            return 26
        elif StaircaseInspection == 12:
            return 26
        else:
            return 26
    else:
        return PatientRoomInspection
 
 
def impute_OfficeInspection(cols):
    OfficeInspection = cols[0]
    PublicAreaRestRoomInspection = cols[1]    
    if pd.isnull(OfficeInspection):
        if PublicAreaRestRoomInspection == 0:
            return 9
        elif PublicAreaRestRoomInspection == 1:
            return 9
        elif PublicAreaRestRoomInspection == 2:
            return 9
        elif PublicAreaRestRoomInspection == 3:
            return 11
        elif PublicAreaRestRoomInspection == 4:
            return 11
        elif PublicAreaRestRoomInspection == 5:
            return 11
        elif PublicAreaRestRoomInspection == 6:
            return 12
        elif PublicAreaRestRoomInspection == 7:
            return 12
        elif PublicAreaRestRoomInspection == 8:
            return 12
        elif PublicAreaRestRoomInspection == 9:
            return 12
        elif PublicAreaRestRoomInspection == 10:
            return 13
        elif PublicAreaRestRoomInspection == 11:
            return 13
        elif PublicAreaRestRoomInspection == 12:
            return 13
        else:
            return 9
    else:
        return OfficeInspection
        

def impute_WaitingAreaInspection(cols):
    WaitingAreaInspection = cols[0]
    SoiledUtilityInspection = cols[1]
    
    if pd.isnull(WaitingAreaInspection):

        if SoiledUtilityInspection == 0:
            return 12
        elif SoiledUtilityInspection == 1:
            return 12
        elif SoiledUtilityInspection == 2:
            return 12
        elif SoiledUtilityInspection == 3:
            return 12
        elif SoiledUtilityInspection == 4:
            return 12
        elif SoiledUtilityInspection == 5:
            return 12
        elif SoiledUtilityInspection == 6:
            return 12
        elif SoiledUtilityInspection == 7:
            return 13
        elif SoiledUtilityInspection == 8:
            return 12
        elif SoiledUtilityInspection == 9:
            return 13
        elif SoiledUtilityInspection == 10:
            return 13
        elif SoiledUtilityInspection == 11:
            return 13
        elif SoiledUtilityInspection == 12:
            return 13           
        else:
            return 12
    else:
        return WaitingAreaInspection


def impute_LiftBankInspection(cols):
    LiftBankInspection = cols[0]
    EntranceInspection = cols[1]
    if pd.isnull(LiftBankInspection):
        if EntranceInspection == 0:
            return 4
        elif EntranceInspection == 1:
            return 4
        elif EntranceInspection == 2:
            return 4
        elif EntranceInspection == 3:
            return 4
        elif EntranceInspection == 4:
            return 6
        elif EntranceInspection == 5:
            return 6
        elif EntranceInspection == 6:
            return 6
        elif EntranceInspection == 7:
            return 7
        elif EntranceInspection == 8:
            return 7.5
        elif EntranceInspection == 9:
            return 10
        elif EntranceInspection == 10:
            return 10
        else:
            return 10
    else:
        return LiftBankInspection


def impute_StaircaseInspection(cols):
    StaircaseInspection = cols[0]
    LiftBankInspection = cols[1]
    if pd.isnull(StaircaseInspection):
        if LiftBankInspection == 0:
            return 6
        elif LiftBankInspection == 1:
            return 8
        elif LiftBankInspection == 2:
            return 10
        elif LiftBankInspection == 3:
            return 8
        elif LiftBankInspection == 4:
            return 9
        elif LiftBankInspection == 5:
            return 9
        elif LiftBankInspection == 6:
            return 10
        elif LiftBankInspection == 7:
            return 9
        elif LiftBankInspection == 8:
            return 10.5
        elif LiftBankInspection == 9:
            return 11
        elif LiftBankInspection == 10:
            return 12
        else:
            return 9
    else:
        return StaircaseInspection


def impute_MedicalWasteRoomInspection(cols):
    MedicalWasteRoomInspection = cols[0]
    HousekeepingClosetInspection = cols[1]    
    if pd.isnull(MedicalWasteRoomInspection):
        if HousekeepingClosetInspection == 0:
            return 6
        elif HousekeepingClosetInspection == 2:
            return 6
        elif HousekeepingClosetInspection == 3:
            return 6
        elif HousekeepingClosetInspection == 4:
            return 6
        elif HousekeepingClosetInspection == 5:
            return 6
        elif HousekeepingClosetInspection == 6:
            return 6
        elif HousekeepingClosetInspection == 7:
            return 6
        elif HousekeepingClosetInspection == 8:
            return 6
        elif HousekeepingClosetInspection == 9:
            return 8
        elif HousekeepingClosetInspection == 10:
            return 9
        elif HousekeepingClosetInspection == 11:
            return 9
        elif HousekeepingClosetInspection == 12:
            return 9
        elif HousekeepingClosetInspection == 13:
            return 9
        elif HousekeepingClosetInspection == 14:
            return 9
        else:
            return 8
    else:
        return MedicalWasteRoomInspection


def impute_PublicAreaRestRoomInspection(cols):
    PublicAreaRestRoomInspection = cols[0]
    StaircaseInspection = cols[1]
    if pd.isnull(PublicAreaRestRoomInspection):
        if StaircaseInspection == 0:
            return 20
        elif StaircaseInspection == 1:
            return 20
        elif StaircaseInspection == 2:
            return 21
        elif StaircaseInspection == 3:
            return 22
        elif StaircaseInspection == 4:
            return 21.5
        elif StaircaseInspection == 5:
            return 21.5
        elif StaircaseInspection == 6:
            return 22
        elif StaircaseInspection == 7:
            return 22
        elif StaircaseInspection == 8:
            return 22
        elif StaircaseInspection == 9:
            return 23
        elif StaircaseInspection == 10:
            return 23
        elif StaircaseInspection == 11:
            return 23
        elif StaircaseInspection == 12:
            return 23
        else:
            return 22
    else:
        return PublicAreaRestRoomInspection


def impute_HousekeepingClosetInspection(cols):
    HousekeepingClosetInspection = cols[0]
    StaircaseInspection = cols[1]
    if pd.isnull(HousekeepingClosetInspection):
        if StaircaseInspection == 0:
            return 8
        elif StaircaseInspection == 1:
            return 11
        elif StaircaseInspection == 2:
            return 11
        elif StaircaseInspection == 3:
            return 12
        elif StaircaseInspection == 4:
            return 12
        elif StaircaseInspection == 5:
            return 13
        elif StaircaseInspection == 6:
            return 12
        elif StaircaseInspection == 7:
            return 12
        elif StaircaseInspection == 8:
            return 12
        elif StaircaseInspection == 9:
            return 13
        elif StaircaseInspection == 10:
            return 13
        elif StaircaseInspection == 10.5:
            return 11
        elif StaircaseInspection == 11:
            return 14
        elif StaircaseInspection == 12:
            return 14
        else:
            return 12
    else:
        return HousekeepingClosetInspection


def impute_SoiledUtilityInspection(cols):
    SoiledUtilityInspection = cols[0]
    PublicAreaRestRoomInspection = cols[1]    
    if pd.isnull(SoiledUtilityInspection):
        if PublicAreaRestRoomInspection == 7:
            return 8
        elif PublicAreaRestRoomInspection == 8:
            return 8
        elif PublicAreaRestRoomInspection == 9:
            return 8
        elif PublicAreaRestRoomInspection == 10:
            return 8
        elif PublicAreaRestRoomInspection == 11:
            return 8
        elif PublicAreaRestRoomInspection == 12:
            return 8
        elif PublicAreaRestRoomInspection == 13:
            return 8
        elif PublicAreaRestRoomInspection == 14:
            return 8
        elif PublicAreaRestRoomInspection == 15:
            return 8
        elif PublicAreaRestRoomInspection == 16:
            return 8
        elif PublicAreaRestRoomInspection == 17:
            return 10
        elif PublicAreaRestRoomInspection == 18:
            return 9
        elif PublicAreaRestRoomInspection == 19:
            return 10
        elif PublicAreaRestRoomInspection == 20:
            return 11
        elif PublicAreaRestRoomInspection == 21:
            return 11
        elif PublicAreaRestRoomInspection == 22:
            return 11
        elif PublicAreaRestRoomInspection == 23:
            return 11
        elif PublicAreaRestRoomInspection == 24:
            return 11
        else:
            return 11
    else:
        return SoiledUtilityInspection


def impute_HousekeepingCartInspection(cols):
    HousekeepingCartInspection = cols[0]
    OfficeInspection = cols[1]    
    if pd.isnull(HousekeepingCartInspection):
        if OfficeInspection == 1:
            return 11
        elif OfficeInspection == 2:
            return 11
        elif OfficeInspection == 3:
            return 11
        elif OfficeInspection == 4:
            return 11
        elif OfficeInspection == 5:
            return 11
        elif OfficeInspection == 6:
            return 10
        elif OfficeInspection == 7:
            return 9
        elif OfficeInspection == 8:
            return 11
        elif OfficeInspection == 9:
            return 11
        elif OfficeInspection == 10:
            return 9
        elif OfficeInspection == 11:
            return 11
        elif OfficeInspection == 12:
            return 11
        else:
            return 11
    else:
        return HousekeepingCartInspection


def impute_CorridorsAndHallwayInspection(cols):
    CorridorsAndHallwayInspection = cols[0]
    EntranceInspection = cols[1]    
    if pd.isnull(CorridorsAndHallwayInspection):
        if EntranceInspection == 0:
            return 6
        elif EntranceInspection == 1:
            return 5
        elif EntranceInspection == 2:
            return 5
        elif EntranceInspection == 3:
            return 10
        elif EntranceInspection == 4:
            return 10
        elif EntranceInspection == 5:
            return 9
        elif EntranceInspection == 6:
            return 10
        elif EntranceInspection == 7:
            return 10
        elif EntranceInspection == 8:
            return 9.5
        elif EntranceInspection == 9:
            return 10
        elif EntranceInspection == 10:
            return 10
        else:
            return 10
    else:
        return CorridorsAndHallwayInspection


def impute_EntranceInspection(cols):
    EntranceInspection = cols[0]
    LiftBankInspection = cols[1]    
    if pd.isnull(EntranceInspection):
        if LiftBankInspection == 0:
            return 7
        elif LiftBankInspection == 1:
            return 7.5
        elif LiftBankInspection == 2:
            return 6
        elif LiftBankInspection == 3:
            return 8
        elif LiftBankInspection == 4:
            return 7
        elif LiftBankInspection == 5:
            return 10
        elif LiftBankInspection == 6:
            return 10
        elif LiftBankInspection == 7:
            return 10
        elif LiftBankInspection == 8:
            return 8
        elif LiftBankInspection == 9:
            return 10
        elif LiftBankInspection == 10:
            return 10
        else:
            return 10
    else:
        return EntranceInspection


def impute_Target_OverallCleanliness_Hospital_Room(cols):
    Target_OverallCleanliness_Hospital_Room = cols[0]
    PatientRoomInspection = cols[1]
    if pd.isnull(Target_OverallCleanliness_Hospital_Room):
        if PatientRoomInspection == 12:
            return 1
        elif PatientRoomInspection == 13:
            return 1
        elif PatientRoomInspection == 14:
            return 1
        elif PatientRoomInspection == 15:
            return 1
        elif PatientRoomInspection == 16:
            return 1
        elif PatientRoomInspection == 17:
            return 1
        elif PatientRoomInspection == 18:
            return 1
        elif PatientRoomInspection == 19:
            return 2
        elif PatientRoomInspection == 20:
            return 2
        elif PatientRoomInspection == 21:
            return 2
        elif PatientRoomInspection == 22:
            return 2
        elif PatientRoomInspection == 23:
            return 2
        elif PatientRoomInspection == 24:
            return 2
        elif PatientRoomInspection == 25:
            return 2
        elif PatientRoomInspection == 26:
            return 2
        elif PatientRoomInspection == 27:
            return 2
        else:
            return 2
    else:
        return Target_OverallCleanliness_Hospital_Room