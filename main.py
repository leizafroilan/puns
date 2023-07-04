from fastapi import Depends, FastAPI
from .routes import pun_route

app = FastAPI()
app.include_router(pun_route.router)