from google_search import generate_urls_from_query
from langchain_community.document_loaders import WebBaseLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_chroma import Chroma
from model import MODEL_FOR_EMBEDDING, MODEL_FOR_RESPONSE
from langchain_community.embeddings import OllamaEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.llms import Ollama

def generate_documents_from_urls(urls: list[str]):
    loader = WebBaseLoader(urls)
    docs = loader.load()
    return docs

def generate_chunks_from_document_list(docs): 
    text_splitter = CharacterTextSplitter(
        chunk_size=5000,
        chunk_overlap = 100, 
        separator= " "
    )
    chunks = text_splitter.split_documents(docs)
    return chunks 

def select_context_text(docs) -> Chroma: 
    embedding_function = OllamaEmbeddings(model=MODEL_FOR_EMBEDDING)
    chroma_db = Chroma.from_documents(docs, embedding_function, collection_metadata={"hnsw:space": "cosine"})
    results = chroma_db.similarity_search(query,2)
    context_text = "\n".join([doc.page_content for doc in results])
    return context_text


def generate_response(query: str) -> str:
    urls = generate_urls_from_query(query, 2)
    docs = generate_documents_from_urls(urls) 
    chunks = generate_chunks_from_document_list(docs)
    
    context_text = select_context_text(chunks)
    prompt = ChatPromptTemplate.from_template("""Answer the following question based only on the provided context:

    <context>
    {context}
    </context>

    Question: {input}""")
    llm = Ollama(model = MODEL_FOR_RESPONSE)
    chain = prompt | llm 
    response = chain.invoke({"input": query, "context": context_text}) 
    return response 

if __name__ == '__main__':
    query = "number of provinces in Argentina"
    response = generate_response(query)
    print(response)