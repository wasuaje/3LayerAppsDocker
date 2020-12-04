from sqlalchemy.orm import Session
from fastapi import Depends

from . import models, schemas


def get_cash(db: Session, cash_id: int):
    return db.query(models.Cash).filter(models.Cash.id == cash_id).first()


def get_cashes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Cash).offset(skip).limit(limit).all()


def create_cash(db: Session, cash: schemas.CashCreate):
    detail_list = []
    db_cash = models.Cash(fecha=cash.fecha,
                          apertura=cash.apertura,
                          cierre=cash.apertura,
                          descripcion=cash.descripcion,
                          monto_apertura=cash.monto_apertura,
                          monto_cierre=cash.monto_cierre,
                          created_on=cash.created_on,
                          status=cash.status)
    db.add(db_cash)
    db.commit()

    for detail in cash.cash_detail:
        db_det_cash = models.CashDetail(monto=detail.monto,
                                        concepto=detail.concepto,
                                        caja_id=db_cash.id)
        db.add(db_det_cash)
        db.commit()
        detail_list.append(db_det_cash)

    db_cash.cash_detail = detail_list
    db.commit()
    db.refresh(db_cash)
    return db_cash


def get_user(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()


# def get_user_by_email(db: Session, email: str):
#     return db.query(models.User).filter(models.User.email == email).first()


# def get_users(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.User).offset(skip).limit(limit).all()


# def create_user(db: Session, user: schemas.UserCreate):
#     fake_hashed_password = user.password + "notreallyhashed"
#     db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
#     db.add(db_user)
#     db.commit()
#     db.refresh(db_user)
#     return db_user


# def get_items(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.Item).offset(skip).limit(limit).all()


# def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
#     db_item = models.Item(**item.dict(), owner_id=user_id)
#     db.add(db_item)
#     db.commit()
#     db.refresh(db_item)
#     return db_item