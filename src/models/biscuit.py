from itertools import count
from pydantic import BaseModel, Field
from typing import Optional

c = count

class Biscuit(BaseModel):
    id: Optional[int] = Field(default_factory=lambda: next(c))
    descricao: str
    preco: float
    imagem: str

class QueryBiscuit(BaseModel):
    id: Optional[int]
    descricao: Optional[str]
    preco: Optional[float]
    imagem: Optional[str]

class Biscuits(BaseModel):
    biscuits : list[Biscuit]
    count: int