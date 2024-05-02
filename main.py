from fastapi import FastAPI
from generate_response import generate_response
import time 

app = FastAPI()
@app.post("/prompt")
async def proccess_query(query: str):
  start_time = time.perf_counter()
  response = generate_response(query)
  end_time = time.perf_counter()
  duration = end_time - start_time
  return {"response" : response,
          "response-time-seconds": duration
          }