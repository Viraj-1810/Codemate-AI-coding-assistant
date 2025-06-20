import streamlit as st
from chains.chat_chain import chat_with_bot
from utils.memory_utils import clear_memory
from io import StringIO
import fitz  # PyMuPDF

# App title and config
st.set_page_config(page_title="CodeMate Copilot", page_icon="🤖", layout="wide")
st.markdown("<h1 style='color:#4A90E2;'>💻 CodeMate</h1><h3>Your AI Coding Assistant</h3>", unsafe_allow_html=True)

# Initialize session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "input_mode" not in st.session_state:
    st.session_state.input_mode = "Markdown"

# Sidebar for viewing and clearing chat history
with st.sidebar:
    st.header("📜 Chat History")
    for i, (sender, msg) in enumerate(reversed(st.session_state.chat_history[-20:])):
        with st.expander(f"{sender} - Message {len(st.session_state.chat_history) - i}"):
            st.markdown(msg)
    st.markdown("---")
    if st.button("🧹 Clear Memory"):
        clear_memory()
        st.session_state.chat_history = []
        st.experimental_rerun()

    st.markdown("---")
    st.subheader("⚙️ Input Mode")
    st.radio("Select input mode:", ["Markdown", "Code"], key="input_mode")

# Main input area
st.subheader("Ask a coding question, paste code, or upload a PDF 👇")
user_input = ""

if st.session_state.input_mode == "Markdown":
    user_input = st.text_area("Your Prompt (Markdown Supported)", height=150)
else:
    user_input = st.code("""# Paste your code here""", language="python")

uploaded_file = st.file_uploader("📄 Upload a PDF (optional)", type="pdf")
if uploaded_file is not None:
    pdf_text = ""
    doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
    for page in doc:
        pdf_text += page.get_text()
    user_input = pdf_text

if st.button("🚀 Submit") and user_input:
    with st.spinner("Thinking..."):
        response = chat_with_bot(user_input)
        st.session_state.chat_history.append(("🧑 You", user_input))
        st.session_state.chat_history.append(("🤖 CodeMate", response))

# Display recent conversation
if st.session_state.chat_history:
    st.markdown("---")
    st.subheader("🧠 Recent Conversation")
    for sender, msg in reversed(st.session_state.chat_history[-6:]):
        st.markdown(f"**{sender}:**")
        st.markdown(msg)
