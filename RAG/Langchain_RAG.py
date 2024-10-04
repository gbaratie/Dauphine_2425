from langchain_cohere import ChatCohere
from langchain_core.messages import HumanMessage

import tqdm
import os
from dotenv import load_dotenv, find_dotenv
from pinecone import Pinecone
from pinecone import PodSpec

from langchain.text_splitter import RecursiveCharacterTextSplitter

from langchain_pinecone import PineconeVectorStore

# loading the API Keys (Cohere, Pinecone) from .env
load_dotenv(find_dotenv(), override=True)

#from langchain_cohere import CohereEmbeddings
import cohere
COHERE_API_KEY = os.environ.get('COHERE_API_KEY')

# Initialize Pinecone library with API key and environment
pinecone = Pinecone(
    api_key=os.environ.get('PINECONE_API_KEY')
)


# Create embeddings instance
co = cohere.Client(COHERE_API_KEY)



# Open text file and read contents into churchill_speech
with open('../Documents/churchill_speech.txt') as f:
    churchill_speech = f.read()

# Create text splitter instance
# check this video about chunk - https://youtu.be/n0uPzvGTFI0?feature=shared
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000, # maximum size of text chunk in number of characters
    chunk_overlap=20, # pecifies the number of overlapping characters between adjacent chunks.
                      # if chunk 1 ends at character 100, chunk 2 will start at character 80
)

# Split the text into chunks
chunks = text_splitter.create_documents([churchill_speech])

chunk_contents = {}
for i in range(len(chunks)):
    chunk_contents[i] = chunks[i].page_content


chunk_contents_list = list(chunk_contents.values())

# Print specific chunks - you can test it
#print(chunks[2]) 
#print(chunks[10].page_content)
print(f'Now you have {len(chunks)}')

#print(chunks[0]) 
#print(chunks[0].page_content) 



# List all indexes in the Pinecone environment
list_indexes = pinecone.list_indexes().to_dict()
print(f"Existing indexes : {list_indexes}")



# Specify name for index
index_name = 'churchill-speech'
#  Check if index already exists
exists = any(index['name'] == index_name for index in list_indexes['indexes'])
print(f"Already existing : {exists}")

#  Check if index already exists
if not exists :
    print(f'Creating index {index_name} ....')

    # Create index with parameters
    pinecone.create_index(index_name, 
                          # Vector dimension - The number of dimensions for vectors in this index
                          dimension=1024, 
                          # Similarity metric 
                          # Distance measure used to compare vectors
                          # 'cosine' measures the cosine similarity between vectors
                          metric='cosine',
                          spec=PodSpec(
                            environment="gcp-starter")
                          )
                        
    print('Done')
else:
    print(f'Index {index_name} already exists!')


# index object
#index = pinecone.Index(index_name)

# Retrieve usage statistics for the index
#index.describe_index_stats()

"""
test_embedding_Cohere = co.embed(
    texts=[chunks[0].page_content], model="embed-english-v3.0", input_type="classification"
)
#print(test_embedding_Cohere)
"""

def cohere_embedding(docs):
    response = co.embed(texts=docs, model="embed-english-v3.0", input_type="classification")
    return response.embeddings


# Take first text chunk 
#first_chunk = chunks[0]

# Embed the text into a vector 
#vector = embeddings.embed_query(first_chunk.page_content)


# Print the chunk
#print(first_chunk.page_content)
# Print the vector
#print(vector)


# Delete any existing indexes
#indexes = pinecone.list_indexes().names()
#for i in indexes:
#  print('Deleting all indexes ... ', end='')
#  pinecone.delete_index(i)
#  print('Done')



# Index the text chunks into Pinecone 
#vector_store = Pinecone_langchain.from_documents(chunks, embeddings, index_name=index_name)

# path to an example text file
#loader = TextLoader("../../modules/state_of_the_union.txt")
#documents = loader.load()
#text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
#docs = text_splitter.split_documents(documents)

# Generate embeddings for each chunk
#embeddings = [cohere_embedding(chunk) for chunk in chunks]

#print(f"Embeddings : {embeddings[0]}")

# Create a Pinecone vector store from the chunks and their embeddings
# Create the PineconeVectorStore from texts and embeddings
print("###Params###")
print(f"##########################")
print(f"##########################")
print(f"chunk : {chunks[0]}")
print(f"##########################")
print(f"##########################")
print(f"chunk : {chunk_contents[0]}")
print(f"##########################")
print(f"##########################")
#print(f"embed : {cohere_embedding(chunk_contents_list)}")

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
"""
# Créer le PineconeVectorStore à partir de Pinecone
vector_store = PineconeVectorStore(index="churchill-speech", embedding=embedding_instance)

"""
# Créer le PineconeVectorStore à partir des textes et des embeddings
vectorstore_from_docs = PineconeVectorStore.from_texts(
    texts=chunk_contents_list,  # Extraire les textes bruts des chunks
    embedding=embedding_instance,  # Utiliser l'instance d'embedding Cohere
    index_name="churchill-speech"
)
print("Vector store created!")


#vectorstore_from_docs = PineconeVectorStore.from_texts(
#    texts=chunk_contents_list,  # Extract raw texts from chunks
#    embedding=cohere_embedding,  # Use the Cohere embedding function
#    index_name="churchill-speech"
#)




# Query text 
query = 'What are the emotions of the speech?'

# Semantic search against indexed chunks
result = vectorstore_from_docs.similarity_search(query)

# Print top result 
print(result)

# Clean output
print('-' * 50)
for r in result:
    print(r.page_content)
    print('-' * 50)