from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from src.application.chat_use_case import ChatUseCase
from src.infrastructure.cohere_adapter import CohereAdapter

app = FastAPI()

class ChatRequest(BaseModel):
    chat_history: list
    message: str

chat_service = CohereAdapter()
chat_use_case = ChatUseCase(chat_service)

@app.get("/")
async def read_root():
    return {"message": "Welcome to the Chat API"}

@app.post("/chat")
async def chat(request: ChatRequest):
    try:
        response = chat_use_case.execute(request.message, request.chat_history)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)