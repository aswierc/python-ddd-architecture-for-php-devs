from fastapi import FastAPI
from src.client.ui.controllers import router as clients
from dotenv import load_dotenv
from config.db import engine, Base, get_db

# required for create schema - create_all
from src.client.domain.entity import ClientEntity

load_dotenv()

app = FastAPI()
app.include_router(clients)

@app.on_event("startup")
async def on_startup():
    Base.metadata.create_all(engine, checkfirst=True)
