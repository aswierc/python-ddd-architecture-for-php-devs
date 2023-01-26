from fastapi import FastAPI
from fastapi_events.handlers.local import local_handler
from fastapi_events.middleware import EventHandlerASGIMiddleware

from src.client.ui.controllers import router as clients
from dotenv import load_dotenv
from config.db import engine, Base, get_db

# required for create schema - create_all
from src.client.domain.entity import ClientEntity

load_dotenv()

app = FastAPI()
app.add_middleware(EventHandlerASGIMiddleware, handlers=[local_handler])

app.include_router(clients)

@app.on_event("startup")
async def on_startup():
    Base.metadata.create_all(engine, checkfirst=True)
