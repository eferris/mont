import json
from mont import ValidationRequest
from Teacher import Administrator
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from Teacher import load_administrators_from_json
from Teacher import get_admin_by_email

#from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],       # Or ["*"] to allow all origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/Data")
def read_data():
    #  get all paid accounts from the admin table
    load_administrators_from_json(filename="Administrator.JSON")
    if len(Administrator._registry):
        json_data = json.dumps([
        getattr(obj, "admin_id", None) 
        for obj in Administrator._registry])

    return json_data
#     return {"message": "Hello from the remote FastAPI server!"}

    
@app.post("/SignIn")
async def sign_in(ValidationRequest: ValidationRequest):
    # validate the email against the admin table
    return {"message": get_admin_by_email(ValidationRequest)}



