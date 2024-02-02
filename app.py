import streamlit as st
from langchain.llms import OpenAI
from langchain.chains.question_answering import load_qa_chain
from langchain.vectorstores import Chroma,Pinecone
from langchain.embeddings.openai import OpenAIEmbeddings
import pinecone
import openai
import os
import asyncio
from utils.helper import *

openai.api_key = os.getenv("OPENAI_API_KEY")

st.title('	:robot_face: :owl:  Chatbot with Guardrails')
prompt =  st.text_input('Enter your prompt')

embeddings = OpenAIEmbeddings(openai_api_key=os.getenv("OPENAI_API_KEY"))


# pinecone.init(
#     api_key="",
#     environment=""
# )
# index_name=""

# llm=OpenAI(temperature=0,openai_api_key="")
# chain=load_qa_chain(llm,chain_type="stuff")

# docsearch = Pinecone.from_existing_index(index_name=index_name, embedding=embeddings)

async def res(prompt):
  if prompt:
    # docs = docsearch.similarity_search(prompt)
    #st.write(chain.run(input_documents=docs,question=prompt))
    res=await rag_rails.generate_async(prompt=prompt)
    st.write(res)
    # coroutine = rag_rails.generate_async(prompt=prompt)
    # asyncio.run(coroutine)
    
async def main(prompt):
  await res(prompt)

asyncio.run(main(prompt))



