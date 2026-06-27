from fastapi import APIRouter

from services.memory_service import MemoryService


router = APIRouter(
    prefix="/session"
)


@router.post("/")
def create_session():

    session_id = MemoryService.create_session(
        "New Chat"
    )

    return {
        "session_id": session_id
    }

@router.get("/")
def get_sessions():

    return MemoryService.get_sessions()


@router.put(
    "/session/{session_id}"
)
def update_session_title(
        session_id: int,
        title: str
):

    MemoryService.update_title(
        session_id,
        title
    )

    return {
        "message": "updated"
    }