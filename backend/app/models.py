from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date, Float
from sqlalchemy.orm import relationship

from .database import Base


class Cash(Base):
    __tablename__ = "caja"

    id = Column(Integer, primary_key=True, index=True)
    fecha = Column(Date, index=True)
    apertura = Column(Date)
    cierre = Column(Date)
    descripcion = Column(String(100))
    monto_apertura = Column(Float, default=0.00)
    monto_cierre = Column(Float, default=0.00)
    status = Column(Integer, default=0)
    created_on = Column(Date)

    cash_detail = relationship("CashDetail", back_populates="cash")


class CashDetail(Base):
    __tablename__ = "caja_detalle"

    id = Column(Integer, primary_key=True, index=True)
    concepto = Column(String(100))
    monto = Column(Float, default=0.00)
    caja_id = Column(Integer, ForeignKey("caja.id"))

    cash = relationship("Cash", back_populates="cash_detail")


class User(Base):
    __tablename__ = "auth_user"

    id = Column(Integer, primary_key=True, index=True)
    password = Column(String)
    last_login = Column(Date)
    is_superuser = Column(Integer, default=0)
    username = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    is_staff = Column(Integer, default=0)
    is_active = Column(Integer, default=0)
    date_joined = Column(Date)