from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel , validator
import sqlite3

def setupDB():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER
        )
    """)
    conn.commit()
    conn.close()

setupDB()

class TextInput(BaseModel):
    
    name: str
    age: int
    @validator("age")
    def validateAge(cls,age:int):
         if age >= 5 and age<=100:
              return age
         raise ValueError("ERROR FOR AGE")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://muzamilalisuleman.github.io/"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_connection():
    conn = sqlite3.connect("database.db")
    return conn, conn.cursor()

def addUser(data: TextInput):
    conn, cursor = get_connection()
    cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", (data.name, data.age))
    conn.commit()
    conn.close()
def deleteUser(id:int):
    conn, cursor = get_connection()
    cursor.execute("DELETE FROM users WHERE id=?",(id,))
    cursor.execute("SELECT * FROM users WHERE id=?",(id,))
    entry = cursor.fetchall()
    msg = "SUCCESS!"
    if len(entry) == 0:
         msg = "NOT FOUND!"
    conn.commit()
    conn.close()
    return msg
def updateUser(data:TextInput,id:int):
    conn, cursor = get_connection()
    cursor.execute("UPDATE users SET name = ? , age = ? where id = ?", (data.name, data.age,id))
    conn.commit()
    conn.close()
    return "SUCESS!"
@app.post("/response/")
def add(dataPosted: TextInput):
    addUser(dataPosted)
    return {"msg": "SUCCESS"}

@app.get("/users")
def get(limit :int = None):
        conn, cursor = get_connection()
        if limit: 
            cursor.execute(f"SELECT * FROM users LIMIT {limit}")
        else:
             cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()
        data = []
        for i in range(0,len(rows)):
             data.append(list(rows[i]))
        conn.close()
        return {"data":data}
@app.get("/users/{id}")
def get(id:int):
        conn, cursor = get_connection() 
        cursor.execute("SELECT * FROM users Where id = ?",(id,))
        rows = cursor.fetchall()
        conn.close()
        return {"data":rows}

@app.delete("/del-user/{id}")
def delete(id:int):
    return {"msg": deleteUser(id)}
@app.put("/update-user/{id}")
def update(id:int,data:TextInput):
     return updateUser(data,id)
     
