from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv(override=True)

llm=ChatGroq(
    model="openai/gpt-oss-120b" 
)

print("My First Chatbot")

history=[]
while True:
    prompt=input("Enter your prompt: ")
    history.append(prompt)
    if prompt=="Exit":
        break
    
    response=llm.invoke(history)
    history.append(response)
    print(response.content)
