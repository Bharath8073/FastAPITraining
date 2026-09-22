from fastapi import FastAPI
from pymongo import AsyncMongoClient
app = FastAPI()
client = AsyncMongoClient("mongodb://localhost:27017/")
db = client["college"]

#select collection
students_collection = db["students"] 

@app.get("/")
async def home():
    return {
        "message":"FastApI with MongoDB is running"
    }

@app.get("/health")
async def health():
    result = await db.command("ping")
    return {"mangodb":"Connected", "ping":result["ok"]}

