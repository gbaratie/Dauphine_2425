import streamlit as st
st.title("📚 Manage Knowledge")
st.caption("🚀 My First Chatbot using RAG Methodology")


#Sidebar with description
with st.sidebar:
    st.markdown("""
                This page demonstrates how to create a knowledge-enabled chatbot using Cohere & Pinecone

                Please follow the instructions provided [here](https://github.com/gbaratie/Dauphine_2425/tree/main/Cohere)     
                """)
            


## Main Page
st.markdown(
        """
        We will use RAG methodology to learn data to an LLM 
        """
        )

if st.button("Remove Data In Pinecone"):
    st.write("Data removed (To Be modify)")

st.markdown("Add file in pinecone")
file = st.file_uploader("Pick a file")
if file:
    st.write(f"File uploaded: {file.name}")


st.title("💬 Chat")
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