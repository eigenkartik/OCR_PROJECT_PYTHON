from fastapi import FastAPI
import uvicorn
app=FastAPI()

cuisine={
 'indian':['samosa','parantha'],
 'mexican':['pasta','pizza']
}

@app.get('/get_items/{name}')
def get_items(name):
 return cuisine.get(name)

@app.get('/hello')
def hello():
 return "Happy Diwali"


# if __name__=="__main__":
#  uvicorn.run(app, host="127.0.0.1", port=8000)














# import cv2
# import re
# import numpy as np
# import os
# from PIL import Image
# import pytesseract
# from pdf2image import convert_from_path
# print(os.getcwd())
# pages=convert_from_path(r'notebooks/docs/prescription/pre_1.pdf')
# # pages[0].show()
# #
# pytesseract.pytesseract.tesseract_cmd=r'C:\Program Files\Tesseract-OCR\tesseract.exe'
# # text=pytesseract.image_to_string(pages[0],lang='eng')
# # print(text)
#
# def preprocess_image(img):
#     gray=cv2.cvtColor(np.array(img),cv2.COLOR_BGR2GRAY)
#     resized_image=cv2.resize(gray,None,fx=1.5,fy=1.5, interpolation=cv2.INTER_LINEAR)
#     processed_image=cv2.adaptiveThreshold(
#         resized_image,
#         255,
#         cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
#         cv2.THRESH_BINARY,
#         61,
#         11
#         )
#     return processed_image
#
# new_image=preprocess_image(pages[0])
# # Image.fromarray(new_image).show()
# text=pytesseract.image_to_string(new_image,lang='eng')
# print(text)
#
# # def get_patient_name(text):
# #     pattern='Patient Information[^\n]*(.*?)\(\d{3}\)'
# #     matches=re.findall(pattern, text, flags=re.DOTALL)
# #     match=matches[0].strip()
# #     # print(match)
# #     date_pattern='((Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[ \d]+)'
# #     date_matches=re.findall(date_pattern, match)
# #     # print(date_matches)
# #     date=date_matches[0][0]
# #
# #     name=match.replace(date, "").strip()
# #     return name
# #
# # pattern='Patient Information(.*?)(\(\d{3}\) \d{3}-\d{4})'
# # match=re.findall(pattern,text,flags=re.DOTALL)
# # number=match[0][1]
# # print(number)
# #
# # pattern="Have you had the Hepatitis B vaccination\?.*(Yes|No)"
# # match=re.findall(pattern,text,flags=re.DOTALL)
# # print(match)
# #
# # pattern="List any Medical Problems \(asthma, seizures, headaches}:(.*)"
# # match=re.findall(pattern,text,flags=re.DOTALL)
# # answer=match[0].strip()
# # print(answer)
#
# def personal_details(text):
#     # pattern1='Name:(.*)Date'
#     # match1=re.findall(pattern1,text)
#     # pattern2='Address:(.*)\n'
#     # match2 = re.findall(pattern2, text)
#     # pattern3='Address:[^\n]*(.*)Directions'
#     # match3=re.findall(pattern3,text,flags=re.DOTALL)
#     # pattern4 = 'Directions:(.*)Refill'
#     # match4 = re.findall(pattern4, text,flags=re.DOTALL)
#     pattern= 'Refill:(.*)\n'
#     match5 = re.findall(pattern, text)
#     # print ('Name:', match1[0].strip())
#     # print('Address:', match2[0].strip())
#     # print('Medicine:', match3[0].strip())
#     # print('Directions:', match4[0].strip())
#     print(match5)
#     print('Refill:', match5[0].strip())
# #
# #
# #
# #
# personal_details(text)