import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv, find_dotenv
import cohere
from langchain_pinecone import PineconeVectorStore
from pinecone import Pinecone
from pinecone import Index

# loading the API Keys (Cohere, Pinecone) from .env
load_dotenv(find_dotenv(), override=True)

#from langchain_cohere import CohereEmbeddings
import cohere
COHERE_API_KEY = os.environ.get('COHERE_API_KEY')

# Create embeddings instance
co = cohere.Client(COHERE_API_KEY)

# Initialize Pinecone library with API key and environment
PINECONE_API_KEY=os.environ.get('PINECONE_API_KEY')
pinecone = Pinecone(
    api_key=os.environ.get('PINECONE_API_KEY')
)

# Initialiser l'application FastAPI
app = FastAPI()


# Initialisation du client Pinecone et connexion à l'index existant
index = Index(index_name="churchill-speech", host="https://churchill-speech-gddbbzj.svc.gcp-starter.pinecone.io", api_key=PINECONE_API_KEY)

class CohereEmbeddings:
    def __init__(self, cohere_client, model_name="embed-english-v3.0"):
        self.cohere_client = cohere_client
        self.model_name = model_name

    def embed_documents(self, texts):
        response = self.cohere_client.embed(
            texts=texts, 
            model=self.model_name, 
            input_type="classification"
        )
        return response.embeddings

    def embed_query(self, text):
        return self.embed_documents([text])[0]
    

# Créer l'instance d'embeddings
embedding_instance = CohereEmbeddings(co)


# Utilisation du vector store existant
vector_store = PineconeVectorStore(index=index, embedding=embedding_instance)





# Modèle de requête pour le corps de la requête
class RAGRequest(BaseModel):
    query: str



# Exemple de requête
query = 'What are the emotions of the speech?'
result = vector_store.similarity_search(query)



@app.post("/retriver")
async def chat(request: RAGRequest):
    try:
        response = vector_store.similarity_search(
            query=request.query
        )
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
