import uuid
from fastapi import FastAPI,Form,UploadFile, File
import uvicorn
from extractor import extract
import os
app=FastAPI()

@app.post('/extract_from_doc')
def extract_from_doc(
        file_format:str=Form(...),
        # ":str" is called type hint and =Form is default value,
        # (...) instead of passing None for the expected value, one can pass ellepsis value(...) to mention dont want to pass anything
        file:UploadFile=File(...),
):
   content=file.file.read()

   file_path="../backend/uploads/"+str(uuid.uuid4())+".pdf"

   with open (file_path,'wb') as f:
       f.write(content)
   try:
      data=extract(file_path,file_format)
   except Exception as e:
       data={
           'error':str (e)
       }
   if os.path.exists(file_path):
       os.remove(file_path)

   return data




if __name__=='__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)