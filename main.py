from fastapi import FastAPI
from fastapi import Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.encoders import jsonable_encoder

from scripts import techcrunch
import json

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")




# Get requests

@app.get('/', response_class=HTMLResponse)
def homePage(request : Request):
    return templates.TemplateResponse(
        "home.html",
        {
            "request" : request,
        }
    )


@app.get('/techcrunch', response_class=HTMLResponse)
def techcrunchPage(request : Request):
    return templates.TemplateResponse(
        "techcrunch.html",
        {
            "request" : request,
        }
    )
    



 



