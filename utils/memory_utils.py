# utils/memory_utils.py

from langchain.memory import ConversationBufferMemory

# Global memory instance to persist across user messages
memory = ConversationBufferMemory(return_messages=True)

def get_memory():
    """Returns the shared conversation memory."""
    return memory

def clear_memory():
    """Clears the conversation memory."""
    memory.clear()
