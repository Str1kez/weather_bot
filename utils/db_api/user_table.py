from utils.db_api.base_model import BaseModel
import sqlalchemy.sql
from sqlalchemy import Integer, Column, String, BigInteger


class User(BaseModel):
    __tablename__ = 'Users'
    request_id = Column(Integer, primary_key=True, autoincrement=True)
    id = Column(BigInteger, nullable=False)
    city = Column(String(20), nullable=False)
    query: sqlalchemy.sql.Select
