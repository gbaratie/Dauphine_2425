import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv
import cohere

# Charger les variables d'environnement à partir du fichier .env
load_dotenv()
COHERE_API_KEY = os.environ.get('COHERE_API_KEY')

if not COHERE_API_KEY:
    raise ValueError("COHERE_API_KEY not found in environment variables")

co = cohere.Client(COHERE_API_KEY)

# Initialiser l'application FastAPI
app = FastAPI()

# Modèle de requête pour le corps de la requête
class ChatRequest(BaseModel):
    chat_history: list
    message: str

@app.post("/chat")
async def chat(request: ChatRequest):
    try:
        response = co.chat(
            chat_history=request.chat_history,
            message=request.message,
        )
        return {"response": response.text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
