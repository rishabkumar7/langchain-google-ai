from langchain_community.llms import Ollama
from langchain_openai import OpenAIEmbeddings
from langchain.prompts import PromptTemplate
from langchain_pinecone import PineconeVectorStore
import os

from dotenv import load_dotenv
load_dotenv()

embeddings = OpenAIEmbeddings()


PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
index_name = "stoic-wisdom"
vector_store = PineconeVectorStore(index_name=index_name, embedding=embeddings, pinecone_api_key=PINECONE_API_KEY)


results = vector_store.similarity_search_with_score("The only thing that is good is virtue, and the only thing that is bad is vice.", k=2,)

print(results)

def help(query):
    llm = Ollama(
      model="gemma"
    )
    docs = vector_store.similarity_search(query, k=2)
  
    prompt = PromptTemplate(
        input_variables=["query", "docs"],
        template = """
        You are a stoic assistant that answers and helps people with dilemma and concerns in life with Stoicism. Here are some relevant stoicism facts from a book that might help you: \n {docs} 
        \n Here is the user query: {query}
        """
        )
    
    chain = prompt | llm
    response = chain.invoke({"query":query, "docs":docs})
    return response