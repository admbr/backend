from typing import Optional
from sqlmodel import SQLModel, Field


class MoradorBase(SQLModel):
    nome: str = Field()
    apelido: Optional[str] = None
    id_apartamento: int
    cpf: str = Field(unique=True, index=True)
    turma: str
    celular: Optional[str]
    email: Optional[str]
    admin: int = Field(default=0)


class MoradorRead(MoradorBase):
    id: int


class MoradorCreate(MoradorBase):
    senha: Optional[str]


class Morador(MoradorBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
