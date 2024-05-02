from pydantic import BaseModel
from typing import List

class SourceModel(BaseModel):
    urls: List[str]
    content_used_as_context: List[str]

class ResponseModel(BaseModel):
    response: str
    sources: SourceModel
    response_time_seconds: float
