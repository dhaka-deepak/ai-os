import requests

from fastapi import APIRouter
from fastapi import HTTPException

from pydantic import BaseModel


router = APIRouter(
    prefix="/chat",
    tags=["Chat"]
)


class ChatRequest(BaseModel):

    session_id: int

    message: str


class ChatResponse(BaseModel):

    response: str


@router.post(
    "/",
    response_model=ChatResponse
)
def chat(request: ChatRequest):

    try:

        response = requests.post(
            "http://localhost:8001/agent/chat",
            json={
                "session_id": request.session_id,
                "message": request.message
            },
            timeout=300
        )

        response.raise_for_status()

        data = response.json()

        return ChatResponse(
            response=data["response"]
        )

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )