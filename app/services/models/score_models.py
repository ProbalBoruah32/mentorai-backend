from pydantic import BaseModel

class ScoreResponse(BaseModel):
    clarity: float
    pacing: float
    fluency: float
    overall: float
    transcript: str
