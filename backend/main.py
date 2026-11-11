
from fastapi import FastAPI
import uvicorn
klu = FastAPI(
    title="AI Tutor",
    description="AI Tutor Pbl Project",
    version="1.0.0",
)

@klu.get("/")
def home():
    return {"message": "Welcome to AI tutor project"}

@klu.get("/demo")
def demo():
    return {"message": "KL University"}

@klu.get("/askquestion")
def ask():
    return {"message": "What is LLM", "Answer": "Large language model"}

@klu.get("/student")
def student():
    return {"id": "1", "Name": "ram", "gender": "male", "Course": "DSA"}

@klu.get("/students")
def getstudents():
    return [
        {"id": "1", "Name": "ram", "gender": "male", "Course": "DSA"},
        {"id": "2", "Name": "shyam", "gender": "male", "Course": "Python"},
        {"id": "3", "Name": "sita", "gender": "female", "Course": "Java"},
    ]

if __name__ == "__main__" :
    uvicorn.run("main:klu",host="127.0.0.1",port=2027,reload=True)