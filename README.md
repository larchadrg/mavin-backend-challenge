# mavin-backend-challenge
API REST based on Langchain to manage user queries and generate a answer based on web results. 

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