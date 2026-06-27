from repositories.session_repository import SessionRepository
from repositories.message_repository import MessageRepository


class MemoryService:

    @staticmethod
    def create_session(title):

        return SessionRepository.create_session(
            title
        )

    @staticmethod
    def get_sessions():

        return SessionRepository.get_sessions()

    @staticmethod
    def save_message(
            session_id,
            sender,
            content
    ):

        MessageRepository.save_message(
            session_id,
            sender,
            content
        )

    @staticmethod
    def get_messages(session_id):

        return MessageRepository.get_messages(
            session_id
        )
        
    @staticmethod
    def update_title(
        session_id,
        title
    ):

        SessionRepository.update_title(
            session_id,
            title
        )