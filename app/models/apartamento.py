from typing import Optional
from sqlmodel import SQLModel, Field


class ApartamentoBase(SQLModel):
    bloco: str
    numero: str


class ApartamentoRead(ApartamentoBase):
    id: int


class ApartamentoCreate(ApartamentoBase):
    pass


class Apartamento(ApartamentoBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
