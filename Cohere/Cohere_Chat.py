import os
from dotenv import load_dotenv
import cohere

# Charger les variables d'environnement à partir du fichier .env
load_dotenv()
COHERE_API_KEY = os.environ.get('COHERE_API_KEY')


co = cohere.Client(COHERE_API_KEY)

response = co.chat(
    chat_history=[
        {"role": "USER", "message": "Who discovered gravity?"},
        {
            "role": "CHATBOT",
            "message": "The man who is widely credited with discovering gravity is Sir Isaac Newton",
        },
    ],
    message="What year was he born?",
    # perform web search before answering the question. You can also use your own custom connector.
    #connectors=[{"id": "web-search"}],
)

print(response)


