from typing import Optional
from datetime import date
from sqlmodel import SQLModel, Field


class PagamentoBase(SQLModel):
    customer_id: str = Field(unique=True)
    deleted: bool
    description: Optional[str]
    value: float
    status: str
    clientpaymentdate: Optional[date]
    confirmeddate: Optional[date]
    datecreated: date
    duedate: date
    invoicenumber: int
    invoiceurl: str
    netvalue: float
    originalduedate: date
    paymentdate: Optional[date]


class PagamentoRead(PagamentoBase):
    id: str = Field(unique=True)


class PagamentoCreate(PagamentoBase):
    pass


class Pagamentos_asaas(PagamentoBase, table=True):
    id: Optional[str] = Field(default=None, primary_key=True)
