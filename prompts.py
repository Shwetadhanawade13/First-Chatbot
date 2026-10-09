from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
load_dotenv(override=tuple)

llm=ChatGroq(model="openai/gpt-oss-120b",
             temperature=0.6)

prompt_template = PromptTemplate.from_template(
    """Analyze the topic: {topic} and give me a structured response in 3 lines theory about it, don't geuss it,
    answer should be one paragraph    """
)

prompt = prompt_template.invoke(
    { "topic": input("Enter your topic : ") }
)

response = llm.invoke(prompt)
print(response.content)