from dotenv import load_dotenv
from langchain.text_splitter import CharacterTextSplitter
from langchain.schema import Document
from langchain_community.embeddings import HuggingFaceEmbeddings # gets depricated warning
#from langchain.vectorstores import FAISS
from langchain_community.vectorstores import FAISS
from langchain_community.llms.octoai_endpoint import OctoAIEndpoint 
from langchain.prompts import ChatPromptTemplate

from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain.prompts import ChatPromptTemplate

import os

load_dotenv() #  reads key-value pairs from a .env file and sets them as environment variables that can be accessed within Python script using os.environ.
OCTOAI_API_TOKEN = os.environ["OCTOAI_API_TOKEN"]

files = os.listdir("./assets")
file_texts = []
for file in files:
    with open(f"./assets/{file}") as f:
        file_text = f.read()
        text_splitter = CharacterTextSplitter.from_tiktoken_encoder(
        chunk_size=512, chunk_overlap=64, 
    )
    texts = text_splitter.split_text(file_text)
    for i, chunked_text in enumerate(texts):
        file_texts.append(Document(page_content=chunked_text, 
                metadata={"doc_title": file.split(".")[0], "chunk_num": i}))


embeddings = HuggingFaceEmbeddings() 

vector_store = FAISS.from_documents(
    file_texts,
    embedding=embeddings
)

llm = OctoAIEndpoint(
        model="meta-llama-3-8b-instruct",
        max_tokens=1024,
        presence_penalty=0,
        temperature=0.1,
        top_p=0.9,
    )
retriever = vector_store.as_retriever()

template="""You are a fashionista. Use the following pieces of retrieved context to answer the question. If you don't know the answer, just say that you don't know. Use three sentences maximum and keep the answer concise.
Question: {question} 
Context: {context} 
Answer:"""
prompt = ChatPromptTemplate.from_template(template)

chain = (
    {"context": retriever, "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)

# temperature = 20
prompt = "What should you wear on a 60°F temperature for both man and woman?"
output = chain.invoke(prompt)
print(output)
