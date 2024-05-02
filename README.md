# mavin-backend-challenge
API REST based on Langchain to manage user queries and generate a answer based on web results. 

## About 
For this project I was asked to build an API with a single endpoint. The client will use it by making a POST petition with a question as a query parameter, and as a response it should get their question answered. 
The sources for answering the question will be obtained with a web scraping tool, and the answer will be generated with a Large Language Model. This program could also be referred as a RAG, which stands for Retrieval Augmented Generation, and it is a technique used for improving an LLM response by providing it with external sources of knowledge.
The technique consists of dividing the documents that act as knowledge sources into smaller chunks, and feeding them into a vector database. Then a query is made to it, asking for chunks with high similarity to our question. The results are then fed into the LLM, and in this way the LLM can give us a more precise answer. 

## How to Run the Code 
To run the code we first need to download Ollama and the models that we will run. This can be done in Linux by running the following lines: 
```
curl -fsSL https://ollama.com/install.sh | sh  
ollama run qwen:0.5b  
ollama run all-minilm
```

The models used can be changed in the model.py file. 
Next we create an environment and download the libraries in requirements.txt

```
python -m venv env  
pip install -r requirements.txt
```

Lastly, we need to set the environment variables for the google search API. 

```
dotenv set GOOGLE_CSE_ID <key>  
dotenv set GOOGLE_API_KEY <key>
```
we can now run the app in a local host by using uvicorn. 

```
uvicorn main:app
```


## Sources
- https://ai.plainenglish.io/building-scalable-large-language-model-llm-apps-509894bc7f6a
- https://www.youtube.com/watch?v=tcqEUSNCn8l
- https://fastapi.tiangolo.com/
- https://python.langchain.com
