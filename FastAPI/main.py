from fastapi import FastAPI, Path, HTTPException, Query
import json

app = FastAPI()

def load_data():
    with open('user.json','r') as f:
        data = json.load(f)
        
    return data

@app.get('/')
def Home():
    return{'Hello':'These is practise On FastAPI'}

@app.get('/user')
def User():
    data = load_data()
    
    return data

@app.get('/user/{user_id}')
def get_id(user_id : int = Path(..., description="Provide the user id", example='001')):
    data = load_data()
    
    for x in data:
        if x['id'] == user_id:
            return x
    
        raise HTTPException(status_code=404,detail="ID not found") 

