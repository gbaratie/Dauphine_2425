from src.domain.chat_service import ChatService

from src.domain.dto.role_message import RoleMessage

class ChatUseCase:
    def __init__(self, chat_service: ChatService):
        self.chat_service = chat_service

    def execute(self, message: str, chat_history: list[RoleMessage]) -> str:
        return self.chat_service.chat(message, chat_history)