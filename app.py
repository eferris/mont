import json
from mont import HttpRequest
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from mont import load_curriculum_from_json
from mont import load_page_from_json
from mont import load_subject_from_json
from mont import load_prerequisite_from_json
from mont import load_poster_from_json
from mont import load_material_from_json
from mont import load_report_from_json
from Teacher import Administrator
from Teacher import load_teacher_from_json
from Teacher import load_administrator_from_json
from Teacher import get_admin_by_email
from Student import load_student_from_json
from Lesson import load_lesson_from_json

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
    load_administrator_from_json(HttpRequest, filename="Administrator.JSON")
    if len(Administrator._registry):
        json_data = json.dumps([
        getattr(obj, "admin_id", None) 
        for obj in Administrator._registry])

    return json_data
#     return {"message": "Hello from the remote FastAPI server!"}

    
@app.post("/SignIn")
async def sign_in(HttpRequest: HttpRequest):
    # validate the email against the admin table
    return {"message": get_admin_by_email(HttpRequest)}


@app.get("/Curriculum")
def read_curriculum():
    result = load_curriculum_from_json(HttpRequest)
    return(result)


@app.get("/Page")
def read_page():
    result=load_page_from_json(HttpRequest)
    return(result)


@app.get("/Subject")
def read_subject():
    result=load_subject_from_json(HttpRequest)
    return(result)


@app.get("/Prerequisite")
def read_prerequisite():
    result=load_prerequisite_from_json(HttpRequest)
    return(result)


@app.get("/Material")
def material():
    result=load_material_from_json(HttpRequest)
    return(result)


@app.get("/Poster")
def read_poster():
    result=load_poster_from_json(HttpRequest)
    return(result)


@app.get("/Report")
def read_report():
    result=load_report_from_json(HttpRequest)
    return(result)


@app.get("/Lesson")
def read_lesson():
    result=load_lesson_from_json(HttpRequest)
    return(result)


@app.get("/Student")
def read_student():
    result=load_student_from_json(HttpRequest)
    return(result)


@app.get("/Teacher")
def read_teacher():
    result=load_teacher_from_json(HttpRequest)
    return(result)

