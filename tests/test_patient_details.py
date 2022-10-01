import pytest
from src.parser_patient_details import PatientDetailParser

@pytest.fixture()
def doc_1_kathy():
    text='''
    17/12/2020

 

    Patient Medical Record
    
    Patient Information Birth Date
    
    Kathy Crawford May 6 1972
    
    (737) 988-0851 Weight’
    
    9264 Ash Dr 95
    
    New York City, 10005 '
    
    United States Height:
    190
    
     
    
     
    
    In Case of Emergency
    ee J
    Simeone Crawford 9266 Ash Dr
    New York City, New York, 10005
    Home phone United States
    (990) 375-4621
    Work phone
    Genera! Medical History
    nn ee
    Chicken Pox (Varicella): Measies:
    IMMUNE
    
    IMMUNE
    Have you had the Hepatitis B vaccination?
    
    No
    
    List any Medical Problems (asthma, seizures, headaches):
    
    Migraine
    
    '''
    return PatientDetailParser(text)

@pytest.fixture()
def doc_2():
    document_text='''
    Patient Medical Record

    Patient Information Birth Date
    
    Jerry Lucas May 2 1998
    
    (279) 920-8204 Weight:
    
    4218 Wheeler Ridge Dr 57
    
    Buffalo, New York, 14201 Height:
    
    United States gnt
    170
    
    In Case of Emergency
    
    - eee
    
    Joe Lucas . 4218 Wheeler Ridge Dr
    Buffalo, New York, 14201
    Home phone United States
    Work phone
    
    General Medical History
    
     
    
    Chicken Pox (Varicelia): Measles: ..
    
    IMMUNE NOT IMMUNE
    
    Have you had the Hepatitis B vaccination?
    
    ‘Yes
    
    | List any Medical Problems (asthma, seizures, headaches):
    N/A
    
    7?
    v
    
     
    
     
    
    17/12/2020
    '''
    return PatientDetailParser(doc_2)

def test_get_patient_name(doc_1_kathy):
    assert doc_1_kathy.get_patient_name()=='Kathy Crawford'


def test_get_patient_number(doc_1_kathy):
    assert doc_1_kathy.get_patient_number()=='(737) 988-0851'

def test_vaccination_status(doc_1_kathy):
    assert doc_1_kathy.get_patient_vaccination_stat()=='No'

def test_medical_history(doc_1_kathy,doc_2):
    assert doc_1_kathy.get_patient_medical_history()=='Migraine'
    assert doc_2.get_patient_medical_history()=='N/A'