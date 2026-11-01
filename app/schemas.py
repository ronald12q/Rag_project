from pydantic import BaseModel


class query(BaseModel):
    pregunta: str
