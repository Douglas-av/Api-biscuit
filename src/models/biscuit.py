from pydantic import BaseModel

class Biscuit(BaseModel):
    id: int
    descricao: str
    preco: float
    imagem: str