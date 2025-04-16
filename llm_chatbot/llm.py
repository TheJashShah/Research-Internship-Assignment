from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
import os 
import pandas as pd

data = pd.read_csv('data/final.csv')
embeddings = OllamaEmbeddings(model="mxbai-embed-large")
model = OllamaLLM(model="llama3.2")

db_location = "./db"
add_docs = not os.path.exists(db_location)

if add_docs:
    documents = []
    ids = []

    for i in range(data.shape[0]):
        document = Document(
            page_content=(data['full_text'][i] + " " + data['subreddit'][i]),
            metadata = {"date": data['date'][i], "votes": data['ups'][i]},
            id = str(i)
        )

        ids.append(str(i))
        documents.append(document)

vector_store = Chroma(
    collection_name='reddit_comments',
    persist_directory=db_location,
    embedding_function=embeddings
)

if add_docs:
    vector_store.add_documents(documents=documents, ids=ids)

retriever = vector_store.as_retriever(
    search_kwargs={"k" : 20}
)

template = """
You an expert in answering questions about a dataset that contains reddit comments with additinal information.

Here are some relevant comments: {comments}

Here is the question to answer: {question}
"""

prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

def response(question):
    
    comments = retriever.invoke(question)
    result = chain.invoke({"comments" : comments, "question" : question})

    print(result)

response("tell me the views on donald trump")