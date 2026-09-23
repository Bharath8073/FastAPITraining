
#This file is the "entry point" of the application

from fastapi import FastAPI

from app.config import settings

from app.database import ping_database
#creating fastAPI app instance 
app = FastAPI(title=settings.App_name)
#This function runs when the server starts up. It checks if the database connection. 

def on_startup() -> None:
    if not ping_database():
        raise RuntimeError("Could not connect to MongoDB")
    print(f"[startup]Connected to MongoDB. App: {settings.App_name}")
#checks basic health check API endpoint & confirms 
#GET / is runnoing & reachable. (/ is considered as 'root') 
@app.get("/",tags=["Health"])
def health_check():
    return {"status": "ok","app":settings.App_NAME}

