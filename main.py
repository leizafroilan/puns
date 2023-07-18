from fastapi import Depends, FastAPI
from code.routes import pun_route
from code.config.auth import users_route

app = FastAPI()
app.include_router(pun_route.router)
app.include_router(users_route.router)