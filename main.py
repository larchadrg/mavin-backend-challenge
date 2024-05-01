from fastapi import FastAPI
from generate_response import generate_response

app = FastAPI()
@app.post("/prompt")
async def proccess_query(query: str):
  response = generate_response(query)
  return {"response" : response}