from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:8000",
    "http://localhost:80",
    "http://localhost:443",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Get requests

async def render_template(template_name: str, request: Request):
    return templates.TemplateResponse(
        template_name,
        {
            "request": request,
        }
    )

@app.get('/', response_class=HTMLResponse)
async def home_page(request: Request):
    return await render_template("home.html", request)

@app.get('/techcrunch', response_class=HTMLResponse)
async def techcrunch_page(request: Request):
    return await render_template("techcrunch.html", request)

@app.get('/hackernews', response_class=HTMLResponse)
async def hackernews_page(request: Request):
    return await render_template("hackernews.html", request)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
