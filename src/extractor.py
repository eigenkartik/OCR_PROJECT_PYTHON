import util
# from PIL import Image
import pytesseract
from pdf2image import convert_from_path
from parser_prescription import PrescriptionParser
from parser_patient_details import PatientDetailParser

pytesseract.pytesseract.tesseract_cmd=r'C:\Program Files\Tesseract-OCR\tesseract.exe'


def extract(file_path,file_format):
    # step1: extract text from pdf file
    document_text= ''
    pages = convert_from_path(file_path)
    if len(pages)>0:
        page=pages[0]
        processed_image= util.preprocess_image(page)
        text= pytesseract.image_to_string(processed_image,lang='eng')
        document_text= '\n' + text
    # return document_text
    # step2: extract fields from text
    if file_format=='prescription':
        extracted_data=PrescriptionParser(document_text).parse()
    elif file_format=='patient_details':
        extracted_data = PatientDetailParser(document_text).parse()
    else:
        raise Exception(f"Invalid document format,{file_format}")
    return extracted_data

if __name__=='__main__':
    data=extract('../backend/notebooks/docs/patient_details/pd_2.pdf',file_format='patient_details')
    print(data)

