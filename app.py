import streamlit as st
import tiktoken
from chains.chat_chain import chat_with_bot
from utils.memory_utils import clear_memory

# Set up page config
st.set_page_config(page_title="CodeMate Copilot", page_icon="🤖", layout="wide")
st.title("💻 CodeMate: Your AI Coding Assistant")

# Token counter function using tiktoken (compatible with LLaMA/GPT tokenization)
def count_tokens(text, model="gpt2"):
    enc = tiktoken.get_encoding(model)
    return len(enc.encode(text))

# Session state init
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "markdown_mode" not in st.session_state:
    st.session_state.markdown_mode = True

# Sidebar controls
with st.sidebar:
    st.header("📜 Chat History")
    for idx, (sender, msg) in enumerate(st.session_state.chat_history):
        with st.expander(f"{sender}", expanded=False):
            st.markdown(msg)

    st.divider()
    st.checkbox("📝 Use Markdown Input", key="markdown_mode")
    if st.button("🧹 Clear Memory"):
        clear_memory()
        st.session_state.chat_history = []
        st.success("Chat history cleared.")

# Main input area
st.subheader("Ask a coding question, upload a PDF, or paste code 👇")
user_input = st.text_area("Your prompt:", key="user_input", height=200)

# Token usage display
if user_input:
    token_count = count_tokens(user_input)
    st.caption(f"🧮 Estimated tokens: {token_count}")

# Handle response
if st.button("🚀 Run") and user_input:
    response = chat_with_bot(user_input)
    st.session_state.chat_history.append(("🧑 You", user_input))
    st.session_state.chat_history.append(("🤖 CodeMate", response))

# Show last 6 messages
if st.session_state.chat_history:
    st.markdown("---")
    st.subheader("🧠 Recent Conversation")
    for sender, msg in reversed(st.session_state.chat_history[-6:]):
        if st.session_state.markdown_mode and sender == "🤖 CodeMate":
            st.markdown(f"**{sender}:**\n{msg}", unsafe_allow_html=True)
        else:
            st.text(f"{sender}: {msg}")
