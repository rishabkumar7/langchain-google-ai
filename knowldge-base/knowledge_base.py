from langchain_openai import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import S3FileLoader
from langchain_community.document_loaders import PyPDFLoader
from langchain_pinecone import Pinecone
import os

from dotenv import load_dotenv
load_dotenv()

embeddings = OpenAIEmbeddings()


loader = PyPDFLoader("stoicism-as-a-way-of-life.pdf")
book = loader.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=2000, chunk_overlap=100)
docs = text_splitter.split_documents(book)
print (docs[0])

#Set up Pinecone

index_name = "stoic-wisdom"
search = Pinecone.from_documents(docs, embeddings, index_name = index_name)

#Example Query
query = "The only thing that is good is virtue, and the only thing that is bad is vice."
results = search.similarity_search(query)

print(results)
