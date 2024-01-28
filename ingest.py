from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.embeddings import HuggingFaceEmbeddings
from langchain_community.embeddings.fastembed import FastEmbedEmbeddings
from langchain.vectorstores import FAISS
from text_to_speech import TTS

DATA_PATH = "data/"
DB_FAISS_PATH = "vectorstores/db_faiss"

#create vector database
def create_vector_db():
    loader = DirectoryLoader(DATA_PATH, glob='*.pdf', loader_cls = PyPDFLoader)
    documents = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size = 500, chunk_overlap = 50)
    text = text_splitter.split_documents(documents)

    embeddings = FastEmbedEmbeddings()
    # embeddings = HuggingFaceEmbeddings(model_name = 'sentence-transformers/all-MiniLM-L6-v2', model_kwargs = {'device' : 'cpu'})

    db = FAISS.from_documents(text, embeddings)
    db.save_local(DB_FAISS_PATH)
    TTS.text_to_speech("Pre-processing of data complete")
    TTS.play_audio()


if __name__ == '__main__':
    create_vector_db()
