import streamlit as st
st.title("💬 RAG")
st.caption("🚀 My First Chatbot using RAG Methodology")
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

