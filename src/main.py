from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_index():
    return {"Hello": "World"}

@app.get("/about")
def about():
    return "My first FastAPI study"

@app.get("/api/v1/hello-world/")
def read_hello_world():
    return {"wht": "road", "where": "k8s", "version": "v1"}