from fastapi import FastAPI
from generate_response import generate_response
from response_model import ResponseModel

app = FastAPI(
  title = "AskMeApp",
  summary = """This API has the purpose of gathering information from the Internet and making a summary of it to
  provide you with a short answer to your questions, including the source of them. """, 
  contact = {
    "name" : "Lara Combina", 
    "mail" : "lara.combina11@gmail.com",
  }
)

@app.post("/prompt")
async def proccess_query(query: str) -> ResponseModel:
  response = generate_response(query)
  return response 