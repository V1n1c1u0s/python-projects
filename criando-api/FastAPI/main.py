from fastapi import FastAPI
from pydantic import BaseModel

#comando - uvicorn main:app --reload para iniciar o server
#localhost:porta/docs para testar a API

app = FastAPI()

#first route
@app.get("/")
def first():
    return {"Hello": "World"}

#model
class User(BaseModel):
    id: int
    email: str
    password: str

#database
db = [
    User(id=1, email="jose@gmail.com", password="#$nk31cHU"),
    User(id=2, email="maria@gmail.com", password="2@8n1As9Jhf")
]

#GetAllUsers route
@app.get("/users")
def get_all_users():
    return db

#GetUserById route
@app.get("/id/{user_id}")
def get_user_by_id(user_id: int):
    for user in db:
        if user.id is user_id:
            return user
    return {"Status": 404, "Message": "User not found!"}

#AddUser route
@app.post("/users")
def add_user(user: User):
    #basic data control 
    for client in db:
        if user.id is client.id:
            return {"Status": 404, "Message": "A user with this ID already exists!"}
        elif '@' not in user.email:
            return {"Status": 404, "Message": "Try a valid Email!"}
        elif user.email == client.email:
            return {"Status": 404, "Message": "A user with this Email already exists!"}
        elif len(user.password) < 6:
            return {"Status": 404, "Message": "Your password is too short!"}
    db.append(user)
    return user