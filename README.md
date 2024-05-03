# mavin-backend-challenge
API REST based on Langchain to manage user queries and generate a answer based on web results. 

## About 
For this project I was asked to build an API with a single endpoint. The client will use it by making a POST petition with a question as a query parameter, and as a response it should get their question answered. 
The sources for answering the question will be obtained with a web scraping tool, and the answer will be generated with a Large Language Model. This program could also be referred as a RAG, which stands for Retrieval Augmented Generation, and it is a technique used for improving an LLM response by providing it with external sources of knowledge.
The technique consists of dividing the documents that act as knowledge sources into smaller chunks, and feeding them into a vector database. Then a query is made to it, asking for chunks with high similarity to our question. The results are then fed into the LLM, and in this way the LLM can give us a more precise answer. 

## Video
<iframe width="560" height="315" src="https://www.youtube.com/embed/GozApD2AJog?si=ZdZH0bzSDfF6lmGN" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

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

## Questions Asked
### How Would I implement Authentication? 
I would follow the official FastAPI documentation guidance on how to use JSON Web Tokens (JWT) for token-based authentication. Clients will need to provide a valid JWT token in the Authorization header to access the endpoint.
### How would I scale up the system to support thousands of requests per hour? 
While FastAPI was created with the idea of building asynchronous apps, this is not the case of ChromaDB and many methods provided by Langchain. Not allowing this behavior is what would make them not scalable. For this usage it is recommended to use a vendor provided vectorbase or deploy it in another server. 
Also, it is important to note that response time is crucially affected by the model chosen for embeddings and the one chosen for generating a response. For personal experience, it took me 30 minutes to generate a response using Llama 3 on my computer. Although there are more lightweight model alternatives, they start being less precise with the answers, for example Qwen sometimes started answering in chinese, since it was trained mainly with english and chinese sources. 
### How would I test the app?
It’s difficult to make unit tests for validating the results of the LLM, since it acts as a blackbox and the answers it can give changes even between executions. Right now, the best way I found to manually evaluate the sources selected and the execution time is by passing them in the response of the API, this way the user can check out how accurate the answer was.
### How would I implement logging capabilities? 
If I have to do this task, I was considering that a good idea for doing this would be using a document based database such as MongoDB for storing all the information related to the transactions where the API was involved. The information contained ideally should be: API requests parameters and responses, with their timestamps and response time, and status codes or errors thrown.

## Sources
- https://ai.plainenglish.io/building-scalable-large-language-model-llm-apps-509894bc7f6a
- https://www.youtube.com/watch?v=tcqEUSNCn8l
- https://fastapi.tiangolo.com/
- https://python.langchain.com
