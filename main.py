from fastapi import FastAPI
import json

app = FastAPI()

# Load JSON data
def load_data():
    
        with open('patients.json', 'r') as f:
            data = json.load(f)
        return data
    
# Home route
@app.get("/")
def hello():
    return {'message': 'Patient Management System API'}

# About route
@app.get("/about")
def about():
    return {'message': 'Fully loaded system'}

@app.get('/view')
def view():
    data=load_data()
    return data

