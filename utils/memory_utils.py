import os
import pickle
from langchain.memory import ConversationBufferMemory

MEMORY_FILE = "memory/session_memory.pkl"

def save_memory(memory: ConversationBufferMemory):
    os.makedirs("memory", exist_ok=True)
    with open(MEMORY_FILE, "wb") as f:
        pickle.dump(memory, f)

def load_memory() -> ConversationBufferMemory:
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "rb") as f:
            return pickle.load(f)
    else:
        return ConversationBufferMemory(return_messages=True)

