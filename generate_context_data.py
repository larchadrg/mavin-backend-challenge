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
        separator=".",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len,
        is_separator_regex=False,
    )
    chunks = text_splitter.split_documents(docs)
    return chunks 

def create_db_from_documents(docs) -> Chroma: 
    embedding_function = OllamaEmbeddings(model=MODEL_FOR_EMBEDDING)
    chroma_db = Chroma.from_documents(docs, embedding_function)
    return chroma_db  

if __name__ == '__main__':
    query = "Como se llama el perro de Milei?"
    urls = generate_urls_from_query(query)

    docs = generate_documents_from_urls(urls) 
    chunks = generate_chunks_from_document_list(docs)
    db = create_db_from_documents(chunks)
    results = db.similarity_search(query)
    context_text = "\n\n---\n\n".join([doc.page_content for doc in results])

    from langchain.chains.combine_documents import create_stuff_documents_chain

    prompt = ChatPromptTemplate.from_template("""Answer the following question based only on the provided context:

    <context>
    {context}
    </context>

    Question: {input}""")
    llm = Ollama(model = MODEL_FOR_RESPONSE)
    chain = prompt | llm 
    response = chain.invoke({"input": query, "context": context_text}) 
    print(response)