from pydantic import BaseModel, Field

class JawabanTerstruktur(BaseModel):
    answer:str = Field(description='The answer to the user question')
    justification:str = Field(description='Justification for the answer')