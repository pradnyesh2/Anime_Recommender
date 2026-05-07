from langchain_chroma import Chroma
from langchain_community.document_loaders import CSVLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings

from dotenv import load_dotenv
load_dotenv()

class VectorStoreBuilder:
    def __init__(self, csv_path:str, persist_dir:str="chroma_db"):
        self.csv_path = csv_path
        self.persist_dir = persist_dir
        self.embedding = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

    def create_and_save_vectorstore(self):
        data = CSVLoader(file_path=self.csv_path, encoding="utf-8").load()

        text = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100).split_documents(data)

        db = Chroma.from_documents(documents=text, embedding=self.embedding, persist_directory=self.persist_dir)
        return db

    def load_vectorstore(self):
        return Chroma(persist_directory=self.persist_dir, embedding_function=self.embedding)