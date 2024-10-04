
# Instructions for Setting Up and Running RAG Part

Welcome 

## 1. Prerequisites
Before you begin, ensure that you have the necessary API key and have updated your dependencies.


### Create Pinecone API KEY
Follow the instructions in this video: <https://youtu.be/_gC9wWWBjmY?si=Z06gAoH7miIhoEKk>

### 
Follow th

### Step 1.1: Obtain a Cohere API Key -- Not needed if you didn't 
- Visit the [Cohere website](https://cohere.ai) and sign up for an API key.
- Once obtained, store this API key in a `.env` file in the root directory of your project. The file should look something like this:

  ```plaintext
  COHERE_API_KEY=your_api_key_here
  ```

### Step 1.2: Update `requirements.txt`

Open the `requirements.txt` file and add the following dependencies:

  ```plaintext
  cohere
  fastapi
  langchain
  pydantic
  langchain_cohere
  langchain_core
  langchain_community
  langchain_chroma
  ```

After updating the file, run the following command to install the new dependencies:

  ```bash
  pip install -r requirements.txt
  ```


