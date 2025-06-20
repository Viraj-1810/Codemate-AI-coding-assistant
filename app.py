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
            with st.expander(f"{sender}", expanded=False):
                st.markdown(f"{msg}")
    else:
        st.write("No messages yet!")

# Main input area
st.subheader("Ask a coding question or paste some code 👇")
user_input = st.text_input("Your prompt", key="input")

# Handle user input
if user_input:
    try:
        response = chat_with_bot(user_input)
        st.session_state.chat_history.append(("🧑 You", user_input))
        st.session_state.chat_history.append(("🤖 CodeMate", response))
    except Exception as e:
        st.session_state.chat_history.append(("🧑 You", user_input))
        st.session_state.chat_history.append(("🤖 CodeMate", "⚠️ Sorry, something went wrong with the AI server. Please try again later."))
        st.error("Groq API returned an error. It might be down or temporarily unavailable.")

# Show recent conversation below input
if st.session_state.chat_history:
    st.markdown("---")
    st.subheader("🧠 Recent Conversation")
    for sender, msg in reversed(st.session_state.chat_history[-6:]):
        st.markdown(f"**{sender}:** {msg}")
