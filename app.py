import os
import streamlit as st
from dotenv import load_dotenv
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from langchain.llms import Groq
from chat_db import init_db, save_chat, fetch_chat_history

# --- Load environment variables ---
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# --- Initialize Streamlit ---
st.set_page_config(page_title="AI Chatbot using GROQ", page_icon="🤖", layout="wide")
st.title("🤖 AI Chatbot using GROQ")
st.write("Upload your PDF and chat intelligently with it!")

# --- Initialize SQLite database ---
init_db()

# --- Sidebar: Chat history display ---
with st.sidebar:
    st.header("💬 Recent Chats")
    chat_history = fetch_chat_history(limit=10)
    if chat_history:
        for chat in chat_history:
            st.markdown(f"🧑 **You:** {chat[0]}")
            st.markdown(f"🤖 **Bot:** {chat[1]}")
            st.caption(f"⏱️ {chat[2]}")
            st.markdown("---")
    else:
        st.info("No chats saved yet.")

# --- PDF Upload ---
uploaded_file = st.file_uploader("📄 Upload a PDF file", type="pdf")

if uploaded_file:
    with st.spinner("Processing PDF..."):
        loader = PyPDFLoader(uploaded_file)
        docs = loader.load()

        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        chunks = text_splitter.split_documents(docs)

        embeddings = HuggingFaceEmbeddings()
        vectorstore = FAISS.from_documents(chunks, embeddings)

        memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
        retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

        llm = Groq(
            model="llama3-70b-8192",
            groq_api_key=GROQ_API_KEY,
            temperature=0.4
        )

        qa_chain = ConversationalRetrievalChain.from_llm(
            llm=llm,
            retriever=retriever,
            memory=memory
        )

        st.success("✅ PDF processed! You can start chatting below.")

        # --- Chat Interface ---
        user_input = st.text_input("Ask a question about the PDF:")

        if user_input:
            with st.spinner("Generating response..."):
                result = qa_chain({"question": user_input})
                response = result["answer"]
                st.markdown(f"**🤖 Answer:** {response}")

                # --- Save chat to SQLite ---
                save_chat(user_input, response)

else:
    st.info("👆 Please upload a PDF to start chatting.")

