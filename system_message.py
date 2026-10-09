from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage,AIMessage,SystemMessage
from dotenv import load_dotenv

load_dotenv(override=True)

""" chatbot with history """
llm=ChatGroq(
    model="openai/gpt-oss-120b",max_tokens=200 
)

print("My First Chatbot")

messages=[
    SystemMessage(content="You are a Funny AI assistant,reply in fun way")
]
# system prompt-->your are a Funny AI assistant,reply in fun way  You are a Angry AI assistant,reply in Angry way

while True:
    prompt=input("Enter your prompt: ")
    messages.append(HumanMessage(content=prompt))
    if prompt=="Exit":
        break
    
    response=llm.invoke(messages)
    messages.append(AIMessage(content=response.content))
    print(response.content)

print(messages)