from langchain.document_loaders import PyPDFLoader
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

# Check if the Pinecone index exists, if not, create it
existing_indexes = pinecone.list_indexes()
if index_name not in existing_indexes:
    # Assuming a vector dimension, replace 768 with the correct dimension for your embeddings
    pinecone.create_index(index_name, dimension=768, metric="cosine")

# Define the path to your documents folder
folder_path = '/home/cdsw/docs'

# List all PDF files in the folder
pdf_files = [file for file in os.listdir(folder_path) if file.endswith('.pdf')]

# Initialize the text splitter and embeddings
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)

# Check if the Pinecone index exists or create it
# Assuming you have a function or method to check and create an index
# This is a placeholder for the actual logic to manage Pinecone indexes

# Iterate over each PDF file
for pdf_file in pdf_files:
    # Construct the full path to the PDF file
    pdf_path = os.path.join(folder_path, pdf_file)
    
    # Load the PDF document
    loader = PyPDFLoader(pdf_path)
    data = loader.load()
    
    # Split the document into chunks of text
    texts = text_splitter.split_documents(data)
    
    # Generate embeddings for each chunk of text
    # Assuming 'from_texts' can handle a list of texts directly; if not, you might need to iterate over 'texts'
    if texts:
        # Flatten the list of texts since 'texts' is a list of lists where each sublist corresponds to a page
        flat_texts = [chunk for page in texts for chunk in page]
        
        # Create or update the Pinecone index with the embeddings
        docsearch = Pinecone.from_texts(flat_texts, embeddings, index_name=index_name)

# At this point, the script processes each PDF, generates embeddings for its text,
# and either creates or updates a Pinecone index with these embeddings.