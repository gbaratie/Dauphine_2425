import streamlit as st
import requests

st.title("💬 Chatbot with Memory")
st.caption("🚀 My First Chatbot using Cohere")
st.markdown(
        """
        On this demonstration we will be able to send request to Cohere and have a chat with history 
        """
        )

#Code copy from https://github.com/streamlit/llm-examples/blob/main/Chatbot.py

api_url="http://127.0.0.1:8000/chat"

with st.sidebar:
    "Here a specific text for Chatbot, even I can add some params"
    x = st.slider('x')  # 👈 this is a widget
    st.write(x, 'squared is', x * x)
    st.text_input("Your name", key="name")
    option = st.selectbox(
    'Selector',
    [1, 2, 3, 4])
    'You selected: ', option
    'Progress Bar'
    bar = st.progress(20)
    file = st.file_uploader("Pick a file")
    color = st.color_picker("Pick a color")
    "More elements following this link : https://docs.streamlit.io/develop/api-reference"




    


# Initialize the chat history
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

# Display the chat history
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# When a user submits a message
if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})
    ##st.chat_message("assistant").write("Hello Buddy")

    # Display the user's message
    st.chat_message("user").write(prompt)

    # Prepare the payload for the API request
    payload = {
        "chat_history": [{"role": "USER", "message": msg["content"]} if msg["role"] == "user" else {"role": "CHATBOT", "message": msg["content"]} for msg in st.session_state.messages],
        "message": prompt
    }
    # Send the request to the API
    try:
        response = requests.post(api_url, json=payload)
        response.raise_for_status()  # Will raise an exception for HTTP errors
        bot_response = response.json().get("response", "I didn't understand that.")
    except requests.exceptions.RequestException as e:
        bot_response = f"Error: {e}"
    
    # Display the bot's response
    st.session_state.messages.append({"role": "assistant", "content": bot_response})
    st.chat_message("assistant").write(bot_response)



