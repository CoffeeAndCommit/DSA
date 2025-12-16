

from sqlalchemy import Column , Integer , String , Float, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class AccountDB(Base):
    __tablename__ = "accounts"


    account_no = Column(Integer, primary_key=True)
    holder_name = Column(String)
    pin = Column(String)
    balance = Column(Float)
    account_type = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)


class TransactionDB(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True)
    account_no = Column(Integer, ForeignKey("accounts.account_no"))
    txn_type = Column(String)
    amount = Column(Float)
    time = Column(DateTime, default=datetime.utcnow)