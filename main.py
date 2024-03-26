from fastapi import FastAPI
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


app = FastAPI()
templates = Jinja2Templates(directory="templates")



@app.get('/', response_class=HTMLResponse)
def homePage(request : Request):
    return templates.TemplateResponse(
        request=request,
        name="home.html",

    )
        
        





