# Import the FastAPI 
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette.requests import Request

# Declare an instance of the FastAPI class.
app = FastAPI()
templates = Jinja2Templates(directory="templates")

# HTTP route and HTTP method.
@app.get("/")
def read_index():
    return {"Hello": "World!"}

@app.get("/api/v1/hello-world/")
def read_hello_world():
    return {"Hello": "World!"}


@app.get("/news", response_class=HTMLResponse)
async def read_news(request: Request):
    news_data = [
        {"headline": "Breaking News Headline 1", "date": "December 11, 2024", "content": "Lorem ipsum dolor sit amet."},
        {"headline": "Breaking News Headline 2", "date": "December 10, 2024", "content": "Suspendisse potenti."},
        {"headline": "Breaking News Headline 3", "date": "December 9, 2024", "content": "Nulla facilisi."},
    ]
    return templates.TemplateResponse("news.html", {"request": request, "news_data": news_data})
