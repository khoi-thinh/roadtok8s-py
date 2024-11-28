# Import the FastAPI class from the fastapi module.
from fastapi import FastAPI
# Declare an instance of the FastAPI class.
app = FastAPI()
# use the app instance as a decorator to handle an
# HTTP route and HTTP method.
@app.get("/")
def read_index():
    return {"Hello": "World!"}

@app.get("/api/v1/hello-world/")
def read_hello_world():
    return {"Konnichiwa": "Minasan"}