import streamlit as st
from chains.chat_chain import chat_with_bot

# App title and config
st.set_page_config(page_title="CodeMate Copilot", page_icon="🤖", layout="wide")
st.title("💻 CodeMate: Your AI Coding Assistant")

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Sidebar for viewing chat history
with st.sidebar:
    st.header("📜 Chat History")
    if st.session_state.chat_history:
        for sender, msg in st.session_state.chat_history:
            st.markdown(f"**{sender}**: {msg}")
    else:
        st.write("No messages yet!")

# Main input area
st.subheader("Ask a coding question or paste some code 👇")
user_input = st.text_input("Your prompt", key="input")

# If user types something
if user_input:
    response = chat_with_bot(user_input)
    st.session_state.chat_history.append(("🧑 You", user_input))
    st.session_state.chat_history.append(("🤖 CodeMate", response))

# Show recent conversation below input
if st.session_state.chat_history:
    st.markdown("---")
    st.subheader("🧠 Recent Conversation")
    for sender, msg in reversed(st.session_state.chat_history[-6:]):  # last 6 messages
        st.markdown(f"**{sender}:** {msg}")
