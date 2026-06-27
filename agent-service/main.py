from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from models.request import ChatRequest
from models.response import ChatResponse

from agents.assistant_agent import AssistantAgent


app = FastAPI(
    title="AI OS Agent Service",
    version="1.0.0"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def health():

    return {
        "service": "agent-service",
        "status": "UP"
    }


@app.post(
    "/agent/chat",
    response_model=ChatResponse
)
def chat(request: ChatRequest):

    response = AssistantAgent.process(
        request.session_id,
        request.message
    )

    return ChatResponse(
        response=response
    )