import os
from dotenv import load_dotenv
import cohere

# Charger les variables d'environnement à partir du fichier .env
load_dotenv()

COHERE_API_KEY = os.environ.get('COHERE_API_KEY')
print(COHERE_API_KEY)

co = cohere.Client(COHERE_API_KEY)

response = co.chat(
	message="hello world!"
)

print(response)