from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from src.database.database import init_db

from src.auth.router import router as user_router

app = FastAPI()

app.include_router(user_router)

@app.get("/")
def read_root():
    html_content = "<h1>Hello, world<h1>"
    return HTMLResponse(content=html_content)

@app.on_event('startup')
async def on_startup():
    await init_db()

