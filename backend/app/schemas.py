from typing import List, Optional
import datetime
from pydantic import BaseModel


class CashDetailBase(BaseModel):
    concepto: str
    monto: float


class CashDetailCreate(CashDetailBase):
    caja_id: int


class CashDetail(CashDetailBase):
    id: int

    class Config:
        orm_mode = True


class CashBase(BaseModel):
    fecha: datetime.datetime
    apertura: Optional[datetime.datetime] = datetime.datetime.now()
    cierre: Optional[datetime.datetime] = datetime.datetime.now()
    monto_apertura: Optional[float] = 0.00
    monto_cierre: Optional[float] = 0.00
    descripcion: Optional[str] = "Descripcion: "
    status: Optional[str] = 0
    created_on: Optional[datetime.datetime] = datetime.datetime.now()
    cash_detail: List[CashDetail] = []


class CashCreate(CashBase):
    pass


class Cash(CashBase):
    id: int

    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None


class User(BaseModel):
    username: str
    email: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    is_active: Optional[bool] = None


class UserInDB(User):
    password: str


# class UserBase(BaseModel):
#     email: str


# class UserCreate(UserBase):
#     password: str


# class User(UserBase):
#     id: int
#     is_active: bool
#     items: List[Item] = []

#     class Config:
#         orm_mode = True