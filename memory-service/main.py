from fastapi import FastAPI

from routers.session_router import router as session_router
from routers.message_router import router as message_router

from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(
    title="AI OS Memory Service"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(session_router)
app.include_router(message_router)