import requests


MEMORY_URL = "http://localhost:8002"


class MemoryClient:

    @staticmethod
    def save_message(
            session_id,
            sender,
            content
    ):

        requests.post(
            f"{MEMORY_URL}/message/",
            json={
                "session_id": session_id,
                "sender": sender,
                "content": content
            }
        )

    @staticmethod
    def get_messages(
            session_id
    ):

        response = requests.get(
            f"{MEMORY_URL}/message/{session_id}"
        )

        return response.json()