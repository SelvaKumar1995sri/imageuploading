from fileinput import filename
from msilib.schema import Binary
from os import access
from turtle import up
from fastapi.responses import FileResponse
from fastapi import FastAPI,File,UploadFile
from pydantic import BaseModel
import pymongo
from bson.binary import Binary

import uvicorn

client = pymongo.MongoClient(
    "mongodb+srv://mongouser:mongopwd@cluster1.davwpcs.mongodb.net/?retryWrites=true&w=majority")
mydata = client['mydatabase']
mycollection = mydata['test_image']

app = FastAPI()
    


@app.post("/images/")
async def create_upload_file(file: bytes = File()):

    mycollection.insert_one({"filename":"file","file": Binary(file),"file_size":len(file)})
    
    return {"Inserted file successfully"}



if __name__=='__main__':
    uvicorn.run("movies:app",reload=True,access_log=True)