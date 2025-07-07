import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.chains.conversation.memory import ConversationBufferMemory
from langchain.chains import ConversationChain

load_dotenv()

llm = ChatGroq(
    model_name="llama3-8b-8192",
    temperature=0.2,
    groq_api_key=os.getenv("GROQ_API_KEY")
)

memory = ConversationBufferMemory(return_messages=True)

chatbot = ConversationChain(
    llm=llm,
    memory=memory,
    verbose=True
)

def chat_with_bot(user_input, mode="explain"):
    prompts = {
        "explain": f"Explain the following code:\n{user_input}",
        "debug": f"Find and fix bugs in the following code:\n{user_input}",
        "refactor": f"Refactor and optimize this code:\n{user_input}",
        "best_practices": f"Suggest best practices for the following code:\n{user_input}"
    }
    prompt = prompts.get(mode, user_input)
    return chatbot.run(prompt)
