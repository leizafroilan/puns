import uvicorn
from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from code.routes.pun_route import router as pun_router
from code.config.auth.users_route import router as auth_router


description = """
PunnyAPI. 🚀

Embrace the pun-tastic possibilities and let the laughter flow freely with every call to our pun-filled API.
"""


# Set up CORS middleware
origins = [
    "http://localhost:3000",  
    "https://127.0.0.1:3000",
    "http://3.15.142.60:9000/"
]


app = FastAPI(
    title="PunnyAPI",
    description=description,
    version="1",
    license_info={
        "name": "MIT License",
    },
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

app.include_router(pun_router)
app.include_router(auth_router)
