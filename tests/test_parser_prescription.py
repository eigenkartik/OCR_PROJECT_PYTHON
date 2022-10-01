from src.parser_prescription import PrescriptionParser
import pytest

@pytest.fixture()
def maria():
    document_text='''
    
        Dr John Smith, M.D
        2 Non-Important Street,
        New York, Phane (000)-111-2222
        
        Name: Maria Sharapova Date: 5/11/2022 
        
        Address: 9 tennis court, new Russia, DC
        
        Prednisone 20 mg
        Lialda 2.4 gram
        
        Directions:
        
        Prednisone, Taper 5 mg every 3 days,
        Finish in 2.5 weeks 
        Lialda - take 2 pill everyday for 1 month 
        
        Refill: 2_times
    
    '''
    return PrescriptionParser(document_text)


@pytest.fixture()
def kartik():
    document_text = '''

        Dr John Smith, M.D
        2 Non-Important Street,
        New York, Phane (000)-111-2222

        Name: Kartik Sharma Date: 5/11/2022 

        Address: 9 tennis court, new Russia, DC

        Prednisone 20 mg
        Lialda 2.4 gram

        Directions:

        Prednisone, Taper 5 mg every 3 days,
        Finish in 2.5 weeks 
        Lialda - take 2 pill everyday for 1 month 

        Refill: 2_times

    '''
    return PrescriptionParser(document_text)


@pytest.fixture()
def blank_doc():
    document_text='''
    '''
    return PrescriptionParser(document_text)


def test_get_name(maria,kartik,blank_doc):
    assert maria.get_field('patient_name')=='Maria Sharapova'
    assert kartik.get_field('patient_name')=='Kartik Sharma'
    assert blank_doc.get_field('patient_name')==None

def test_get_address(maria):
    assert maria.get_field('patient_address')=='9 tennis court, new Russia, DC'


def test_medicine(maria):
    assert maria.get_field('patient_medicine')=='''Prednisone 20 mg
        Lialda 2.4 gram'''

def test_direction(maria):
    assert maria.get_field('medicine_direction')=='''Prednisone, Taper 5 mg every 3 days,
        Finish in 2.5 weeks 
        Lialda - take 2 pill everyday for 1 month'''


def test_med_refill(maria):
    assert maria.get_field('medicine_refill')=='2_times'