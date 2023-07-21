import uvicorn
from fastapi import Depends, FastAPI
from code.routes.pun_route import router as pun_router
from code.config.auth.users_route import router as auth_router


description = """
PunnyAPI. 🚀

Embrace the pun-tastic possibilities and let the laughter flow freely with every call to our pun-filled API.
"""

app = FastAPI(
    title="PunnyAPI",
    description=description,
    version="1",
    license_info={
        "name": "MIT License",
    },
)

app.include_router(pun_router)
app.include_router(auth_router)
