from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate

from dotenv import load_dotenv
load_dotenv()

def ask_stoic(query):
    """
    This function takes a query as input, invokes the language model with the query,
    and returns the response from the language model.

    Parameters:
    query (str): The question to ask the language model.

    Returns:
    str: The response from the language model.
    """

    # Initialize the language model
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

#   llm = Ollama(model="gemma")

    prompt = PromptTemplate(
        input_variables=["query"],
        template = """
        You are a stoic assistant that answers and helps people with dilemma and concerns in life with Stoicism. Here is the user query: {query}
        """
    )

    chain = prompt | llm

    response = chain.invoke({"query":query})
    return response.content

print(ask_stoic("How to stay calm in difficult situations?"))