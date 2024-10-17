from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from src.database.database import init_db

app = FastAPI()

@app.get("/")
def read_root():
    html_content = "<h1>Hello, world<h1>"
    return HTMLResponse(content=html_content)

@app.on_event('startup')
async def on_startup():
    await init_db()