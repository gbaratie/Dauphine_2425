from langchain_cohere import ChatCohere
from langchain_core.messages import HumanMessage


load_dotenv()
COHERE_API_KEY = os.environ.get('COHERE_API_KEY')

chat = ChatCohere(cohere_api_key=COHERE_API_KEY)
messages = [HumanMessage(content="knock knock")]
#print(chat.invoke(messages))
print(chat.invoke(messages).content)







