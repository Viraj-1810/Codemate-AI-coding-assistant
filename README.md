# 💻 CodeMate: Your AI Coding Assistant

CodeMate is an intelligent, real-time AI Copilot designed to help developers write, understand, debug, and improve code effortlessly. Built with **Streamlit**, powered by **Groq's blazing-fast LLaMA 3**, and enhanced by **LangChain**, it supports contextual memory, markdown/code toggle, chat history, and PDF parsing.

---

## 🚀 Features

✅ **Answer Coding Questions**  
> _"What does this function do?"_  
> _"What's the difference between an interface and an abstract class?"_

✅ **Chat with Memory**  
Multi-turn conversations with context awareness:  
> _You: How do I create a list in Python?_  
> _You: Now convert it to a set._

✅ **Explain Code Snippets**  
Paste any code and get a line-by-line explanation.

✅ **Suggest Code Improvements**  
Get optimized, readable, and cleaner versions with rationale.

✅ **Debug Logic Errors**  
Paste buggy code and get suggestions and fixes.

✅ **Suggest Best Practices**  
Follows Pythonic conventions and secure coding principles.

✅ **Markdown/Code Toggle Input**  
Choose between markdown notes or code-based prompts.

✅ **PDF Parsing (Code from Docs)**  
Upload `.pdf` files — extract and discuss code from them.

✅ **Collapsible Chat History**  
Easily navigate past messages with toggle support in sidebar.

✅ **Export Chat History (Coming Soon)**  
One-click download of your session as `.txt` or `.md`.

---

## 🛠️ Tech Stack

- [Streamlit](https://streamlit.io/)
- [LangChain](https://www.langchain.com/)
- [Groq API](https://console.groq.com/)
- [LLaMA 3 8B](https://huggingface.co/meta-llama)
- [PyMuPDF](https://pymupdf.readthedocs.io/en/latest/) for PDF parsing

---

## 📁 Project Structure

codemate/
│
├── app.py # Main Streamlit app
├── requirements.txt # All dependencies
│
├── chains/ # Contains LangChain logic
│ ├── chat_chain.py
│
├── utils/ # Memory and helper utilities
│ └── memory_utils.py
│
└── assets/ # (Optional) For icons or UI enhancements


---

## 📦 Setup Instructions

```bash
# 1. Clone the repo
git clone https://github.com/your-username/codemate.git
cd codemate

# 2. (Optional) Create a virtual environment
python -m venv venv
venv\Scripts\activate    # On Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Add your Groq API key
# Inside app.py or use environment variable
os.environ["GROQ_API_KEY"] = "your-groq-api-key"

# 5. Run the app
streamlit run app.py
👤 Developed by
Viraj Gupta
Final Year Student, Jaypee University of Engineering and Technology
