from langchain_community.llms import Ollama

llm = Ollama(
    model="gemma"
)

response = llm.invoke("Tell me a joke")
print(response)