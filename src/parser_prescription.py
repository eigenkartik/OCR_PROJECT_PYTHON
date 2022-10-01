from src.generic_parser import MedicalDocParser
import re


class PrescriptionParser(MedicalDocParser):
    def __init__(self,text):
        MedicalDocParser.__init__(self,text)

    def parse(self):
        return {
            'patient_name':self.get_field('patient_name'),
            'patient_address':self.get_field('patient_address'),
            'patient_medicine':self.get_field('patient_medicine'),
            'medicine_direction':self.get_field('medicine_direction'),
            'medicine_refill':self.get_field('medicine_refill')
        }


    def get_field(self,field_name):
        pattern_dict={
            'patient_name':{'pattern':'Name:(.*)Date','flags':0},
            'patient_address': {'pattern': 'Address:(.*)\n', 'flags': 0},
            'patient_medicine': {'pattern': 'Address:[^\n]*(.*)Directions', 'flags': re.DOTALL},
            'medicine_refill': {'pattern': 'Refill:(.*)', 'flags': 0},
            'medicine_direction': {'pattern': 'Directions:(.*)Refill', 'flags': re.DOTALL}

        }
        pattern_obj=pattern_dict.get(field_name)
        if pattern_obj:
            matches=re.findall(pattern_obj['pattern'],self.text,flags=pattern_obj['flags'])
            if len(matches)>0:
                return matches[0].strip()

    # def get_name(self):
    #     pattern = 'Name:(.*)Date'
    #     match = re.findall(pattern, self.text)
    #     if len(match)>0:
    #         return match[0].strip()
    #
    #
    # def get_address(self):
    #     pattern= 'Address:(.*)\n'
    #     match = re.findall(pattern, self.text)
    #     if len(match)>0:
    #         return match[0].strip()
    #
    # def medicine(self):
    #     pattern = 'Address:[^\n]*(.*)Directions'
    #     match = re.findall(pattern, self.text, flags=re.DOTALL)
    #     if len(match) > 0:
    #         return match[0].strip()
    #
    # def get_direction(self):
    #     pattern = 'Directions:(.*)Refill'
    #     match = re.findall(pattern, self.text, flags=re.DOTALL)
    #     if len(match)>0:
    #         return match[0].strip()
    #
    # def get_refill(self):
    #     pattern = 'Refill:(.*)\n'
    #     match = re.findall(pattern, self.text, flags=re.DOTALL)
    #     if len(match) > 0:
    #         return match[0].strip()


if __name__=='__main__':
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
    
    Refill: 2 times
    
    '''

    pp=PrescriptionParser(document_text)
    print(pp.parse())