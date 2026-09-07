from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langchain_ollama.chat_models import ChatOllama

class MyLLMChatModel:
    
    list_of_chats = []

    # default models
    model = "llama3.2:latest"

    # Default is none
    chat_ollama = None

    def __init__(self, my_model):
        # print(my_model)
        self.model = my_model
        self.chat_ollama = ChatOllama(model=self.model)

        # defnie system message
        self.list_of_chats.append(SystemMessage("You are assitant named NoSys, you always answert the question with sufix three XXX."))
    
    def chat_models(self, new_chat:str):
        # Human message
        self.list_of_chats.append(HumanMessage(new_chat))

        response = self.chat_ollama.invoke(self.list_of_chats)
        print(response.content)
        
        # AIMessage
        self.list_of_chats.append(response)