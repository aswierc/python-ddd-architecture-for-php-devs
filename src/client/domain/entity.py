from datetime import datetime
from pydantic import Field
from config.db import Base
from sqlalchemy import Column, String, Integer, DateTime


class ClientEntity(Base):
    __tablename__ = 'client'
    id: Column | int = Column(Integer, primary_key=True, index=True)
    uuid: Column | str = Column(String, index=True, nullable=False)
    username: Column | str = Column(String, index=True, nullable=False)
    created_at: Column | datetime = Field(sa_column=Column(DateTime(timezone=True), default=datetime.utcnow))

    def __init__(self, username: str, uuid: str):
        self.username = username
        self.uuid = uuid

    def get_username(self) -> str | Column:
        return self.username
