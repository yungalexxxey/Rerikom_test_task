from sqlalchemy import Column, Integer, String
from .alchemy import Base


class DbMsg(Base):
    __tablename__ = 'main_table'
    id = Column(Integer)
    message_id = Column(Integer, primary_key=True, index=True)
    message = Column(String)
    status = Column(String)
