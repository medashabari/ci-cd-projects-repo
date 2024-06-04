import uvicorn
from fastapi import FastAPI,Request
from fastapi.responses import HTMLResponse 
from starlette.templating import Jinja2Templates


app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/",response_class=HTMLResponse)
async def home(request:Request):
    return templates.TemplateResponse("index.html",context={"request":request})

@app.get("/health",response_class=HTMLResponse)
async def home(request:Request):
    return templates.TemplateResponse("health.html",context={"request":request})

if __name__ == '__main__':
    uvicorn.run(app=app,host="0.0.0.0", port=8000)