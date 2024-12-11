# Import the FastAPI 
from fastapi import FastAPI

# Declare an instance of the FastAPI class.
app = FastAPI()

# HTTP route and HTTP method.
@app.get("/")
def read_index():
    return {"Hello": "World!"}

@app.get("/api/v1/hello-world/")
def read_hello_world():
    return {"Hello": "Morning"}
