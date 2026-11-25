import os
from dotenv import load_dotenv
from langchain_nvidia_ai_endpoints import ChatNVIDIA
load_dotenv()


llm=ChatNVIDIA(model=os.getenv("NVIDIA_CHAT_MODEL"),
               temperature=0.7)

response=llm.invoke("Explain Artificial Intelligence in simple language.")
print(response.content)


#prompt Template
from langchain_core.prompts import ChatPromptTemplate
prompt=ChatPromptTemplate.from_template("""
You are an expert educational content writer.
Generate content about the following topic:
Topic:{topic}
Content Type:{content_type}
Writing style:{style}
Word Limit:{word_limit}
write clear,meaninggful and well_structured content.""")

prompt_value=prompt.invoke({
    "topic":"Artificial Intelligence",
    "content_type":"Eductational Explanation",
    "style":"Beginner Friendly",
    "word_limit":300
})
print(prompt_value)
#connect prompt with llm 
from langchain_core.output_parsers import StrOutputParser
chain=prompt | llm |StrOutputParser()

#Generate content Dynamically 
def generate_content(topic, content_type, style, word_limit):
    result=chain.invoke({
        "topic": "Artificial Intelligence",

        "content_type": "Educational Explanation",

        "style": "Beginner Friendly",

        "word_limit": 300

    })

    return result
