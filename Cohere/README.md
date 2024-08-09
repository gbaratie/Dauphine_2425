
# Instructions for Setting Up and Running Cohere Part

Welcome to this project! Follow the steps below to set up your environment, run the provided scripts, and build your own API and graphical interface using Streamlit.

## 1. Prerequisites

Before you begin, ensure that you have the necessary API key and have updated your dependencies.

### Step 1.1: Obtain a Cohere API Key
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
  ```

After updating the file, run the following command to install the new dependencies:

  ```bash
  pip install -r requirements.txt
  ```

## 2. Run the Cohere Prompt Script

### Step 2.1: Execute `Cohere_prompt.py`

- This script allows you to send a prompt to the Cohere API and receive a response.
- You can customize the behavior of the chatbot by modifying the `message` variable within the script.

To run the script:

  ```bash
  python Cohere_prompt.py
  ```

## 3. Run the Cohere Chat Script

### Step 3.1: Execute `Cohere_Chat.py`

- This script enables a conversation with Cohere's API, maintaining a conversation history.
- Inside this file, you can also uncomment lines to enable a web search before making a request to the API.

To run the script:

  ```bash
  python Cohere_Chat.py
  ```

## 4. Create an API Using FastAPI

### Step 4.1: Set Up and Run the FastAPI Server

We will use FastAPI to create an API. You can do this by executing the `FastAPI.py` file.

To start the FastAPI server, run the following command:

  ```bash
  uvicorn FastAPI:app --reload
  ```

### Step 4.2: Test the API

You can interact with your API using Swagger UI, which is automatically provided by FastAPI, or using a tool like Postman.

Access the Swagger UI by navigating to:

  ```
  http://127.0.0.1:8000/docs
  ```

## 5. Create a Graphical Interface with Streamlit

### Step 5.1: Build the Interface

Finally, we will create a graphical interface for our API using Streamlit.

You can develop and customize the interface by writing a Streamlit script and then running it with:

  ```bash
  streamlit run your_streamlit_script.py
  ```
