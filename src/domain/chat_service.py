from abc import ABC, abstractmethod

from src.domain.dto.role_message import RoleMessage

class ChatService(ABC):
    @abstractmethod
    def chat(self, message: str, chat_history: list[RoleMessage]) -> str:
        pass
