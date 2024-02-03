
from langchain.document_loaders import UnstructuredPDFLoader, OnlinePDFLoader,PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Pinecone
from langchain.embeddings.openai import OpenAIEmbeddings
import os
import pinecone

# Initialize Pinecone and OpenAI API
pinecone.init(
    api_key=os.getenv("PINECONE_API_KEY"),
    environment=os.getenv("PINECONE_ENVIRONMENT")
)
openai_api_key = os.getenv("OPENAI_API_KEY")
index_name = os.getenv("PINECONE_INDEX")

embeddings = OpenAIEmbeddings(
    openai_api_key=os.getenv("OPENAI_API_KEY")
    # openai_api_base=OPENAI_API_BASE, 
    # openai_api_type=OPENAI_API_TYPE, 
    # openai_api_version=OPENAI_API_VERSION,
    # chunk_size=1
)

# Check if the Pinecone index exists, if not, create it
existing_indexes = pinecone.list_indexes()
if index_name not in existing_indexes:
    pinecone.create_index(index_name, dimension=1536, metric="cosine")
    
# Initialize Pinecone index object
index = pinecone.Index(index_name)

# Define the path to your documents folder
folder_path = '/home/cdsw/docs'

# List all PDF files in the folder
pdf_files = [file for file in os.listdir(folder_path) if file.endswith('.pdf')]

for pdf_file in pdf_files:
    print(pdf_file)
    loader = PyPDFLoader(folder_path + "/" + pdf_file)
    data = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    texts = text_splitter.split_documents(data)
    docsearch = Pinecone.from_texts([t.page_content for t in texts], embeddings, index_name=index_name)
    print("Loaded PDF document " + pdf_file + " successfully to Pinecone index " + index_name)
    
#     text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
#     texts = text_splitter.split_documents(data)
#     embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)
#     docsearch = Pinecone.from_texts([t.page_content for t in texts], embeddings, index_name=index_name)



