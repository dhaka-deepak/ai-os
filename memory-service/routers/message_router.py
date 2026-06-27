from fastapi import APIRouter

from services.memory_service import MemoryService

from models.message import ChatMessage


router = APIRouter(
    prefix="/message"
)


@router.post("/")
def save_message(
        message: ChatMessage
):

    MemoryService.save_message(
        message.session_id,
        message.sender,
        message.content
    )

    return {
        "status": "saved"
    }


@router.get("/{session_id}")
def get_messages(
        session_id: int
):

    return MemoryService.get_messages(
        session_id
    )
    
