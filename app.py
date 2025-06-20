import streamlit as st
from chains.chat_chain import chat_with_bot

# App title and layout
st.set_page_config(page_title="CodeMate Copilot", page_icon="🤖", layout="wide")
st.title("💻 CodeMate: Your AI Coding Assistant")

# Secure Groq API Key (from secrets)
groq_api_key = st.secrets["GROQ_API_KEY"]

# Initialize chat history and visibility toggle
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "show_history" not in st.session_state:
    st.session_state.show_history = True

# Sidebar for toggling chat history
with st.sidebar:
    st.header("⚙️ Settings")
    toggle = st.button("📜 Toggle Chat History")
    if toggle:
        st.session_state.show_history = not st.session_state.show_history

    if st.session_state.show_history:
        st.markdown("### 📚 Chat History")
        if st.session_state.chat_history:
            for sender, msg in st.session_state.chat_history:
                st.markdown(f"**{sender}**: {msg}")
        else:
            st.write("No messages yet!")

# Main input area
st.subheader("Ask a coding question or paste code 👇")
user_input = st.text_input("Your prompt", key="input")

# Process user input
if user_input:
    with st.spinner("CodeMate is thinking..."):
        response = chat_with_bot(user_input, groq_api_key, st.session_state.chat_history)
        st.session_state.chat_history.append(("🧑 You", user_input))
        st.session_state.chat_history.append(("🤖 CodeMate", response))

# Show recent conversation in collapsible section
if st.session_state.chat_history:
    with st.expander("🧠 Recent Conversation", expanded=True):
        for sender, msg in reversed(st.session_state.chat_history[-6:]):
            st.markdown(f"**{sender}:** {msg}")
