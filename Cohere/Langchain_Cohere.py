from langchain_cohere import ChatCohere
from langchain_core.messages import HumanMessage

chat = ChatCohere(cohere_api_key='hKCbbZk3KOmbmlHRBR5ZsMk3Emcfgb4Fp34kXVhO')
messages = [HumanMessage(content="knock knock")]
#print(chat.invoke(messages))
print(chat.invoke(messages).content)







