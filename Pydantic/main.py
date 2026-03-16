from pydantic import BaseModel, EmailStr, Field
from typing import Dict, List, Annotated

class User(BaseModel):
    name:str
    age:Annotated[int, Field(gt=0,le=120, strict=True)]
    hobbies:Annotated[List[str],Field(max_length=15)]
    email : EmailStr
    
    
def show_data(user : User):
    print(user.name)
    print(user.age)
    print(user.email)
    print(user.hobbies)
    
user_info = {'name':'Raju','age':30, 'email':'abc@gmail.com','hobbies':['Playing','Dancing','Singing']}

user = User(** user_info)

show_data(user)
