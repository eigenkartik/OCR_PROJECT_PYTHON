from src.generic_parser import MedicalDocParser
import re


class PatientDetailParser(MedicalDocParser):
    def __init__(self,text):
        MedicalDocParser.__init__(self,text)

    def parse(self):
        return {
            'patient_name':self.get_patient_name(),
            'phone_number':self.get_patient_number(),
            'hepatitis_b_vaccination':self.get_patient_vaccination_stat(),
            'medical_history':self.get_patient_medical_history()
        }

    def get_patient_name(self):
        pattern = 'Patient Information[^\n]*(.*?)\(\d{3}\)'
        matches = re.findall(pattern, self.text, flags=re.DOTALL)
        match = matches[0].strip()
        # print(match)
        date_pattern = '((Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[ \d]+)'
        date_matches = re.findall(date_pattern, match)
        # print(date_matches)
        date = date_matches[0][0]

        name = match.replace(date, "").strip()
        return name

    def get_patient_number(self):
        pattern = 'Patient Information(.*?)(\(\d{3}\) \d{3}-\d{4})'
        match = re.findall(pattern, self.text, flags=re.DOTALL)
        number = match[0][1]
        return number

    def get_patient_vaccination_stat(self):
        pattern = "Have you had the Hepatitis B vaccination\?.*(Yes|No)"
        match = re.findall(pattern, self.text, flags=re.DOTALL)
        return match[0]

    def get_patient_medical_history(self):
        pattern = "List any Medical Problems \(asthma, seizures, headaches[^\n]:(.*)"
        match = re.findall(pattern, self.text, flags=re.DOTALL)
        answer=match[0].strip()
        return answer


if __name__=='__main__':
    document_text='''
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

    

    pp=PatientDetailParser(document_text)
    print(pp.parse())