CodeMate AI Coding Assistant

A smart developer-assistant tool built with Streamlit, LangChain, Groq’s LLaMA 3 API, and memory support — designed to help you explain, debug, refactor, and craft code with context and continuity.

🚀 Features

Interactive chat interface where you can ask coding questions, request explanations, debug code, or refactor functions.

Supports mode selection tabs: Explain, Debug, Refactor (and can be extended with more).

Maintains persistent session memory so the assistant “remembers” earlier messages in the session.

Allows streamed responses (when supported by the API) for a fluid user experience.

Clean UI with syntax-highlighted code blocks, markdown support, theme toggle (light/dark) and exportable chat history.

Built in Python using Streamlit for web UI, LangChain for conversation & memory management, and Groq’s LLaMA 3 for generation.

🛠️ Technology Stack

Python (backend logic, model integration)

Streamlit (UI)

LangChain (conversation + memory handling)

Groq LLaMA 3 API (large-language-model generation)

SQLite (optional) or other databases for storing session memory / chat history

GitHub for version control

Deployable on platforms like AWS EC2 or Azure App Service

✅ Getting Started

Clone the repository:

git clone https://github.com/Viraj-1810/Codemate-AI-coding-assistant.git
cd Codemate-AI-coding-assistant


Install dependencies:

pip install -r requirements.txt


Set your environment variables (e.g., GROQ_API_KEY, OTHER_API_KEYS, etc.).

Run the app:

streamlit run app.py


Open the URL shown by Streamlit (usually http://localhost:8501) and start interacting with the assistant.

🎯 Why This Matters

In modern software development, having an AI-powered coding assistant accelerates productivity, improves code quality, and offers real-time support for debugging, refactoring, or understanding unfamiliar code. This project shows your ability to integrate cutting-edge AI models, build interactive web apps, manage conversation and memory state, and deliver a deployable product.

👤 Author

Viraj Gupta – Developer & AI Enthusiast
For any questions, feel free to open an issue or drop a message.

📝 License

Specify your license here (e.g., MIT License) if applicable.
