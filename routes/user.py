from fastapi import APIRouter
from config.db import conn
from models.index import users
from schemas.index import User
user = APIRouter()

@user.get("/")
async def read_data():
    return conn.execute(user.select()).fetchall() 

@user.get("/{id}")
async def read_data(id:int):
    return conn.execute(user.select().where(users.c.id == id)).fetchall()

@user.post("/")
async def write_data(user : User):
    conn.execute(users.insert().values(
        name =  user.name ,
        email = user.email ,
        password = user.email
    ))
    return conn.execute(user.select()).fetchall()

    # @user.get("/")
    # async def read_data():
    #     return conn.execute(user.select()).fetchall()