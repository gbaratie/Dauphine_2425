import os
from dotenv import load_dotenv
import cohere
from src.domain.chat_service import ChatService

load_dotenv()
COHERE_API_KEY = os.environ.get('COHERE_API_KEY')

class CohereAdapter(ChatService):
    def __init__(self):
        self.client = cohere.Client(COHERE_API_KEY)

    def chat(self, message: str, chat_history: list) -> str:
        response = self.client.chat(
            chat_history=chat_history,
            message=message
        )
        return response.text