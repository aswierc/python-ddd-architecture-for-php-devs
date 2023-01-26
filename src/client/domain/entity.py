from datetime import datetime
from pydantic import Field
from config.db import Base
from sqlalchemy import Column, String, Integer, DateTime


class ClientEntity(Base):
    __tablename__ = 'client'
    id: int = Column(Integer, primary_key=True, index=True)
    uuid: str = Column(String, index=True, nullable=False)
    username: str = Column(String, index=True, nullable=False)
    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), default=datetime.utcnow))

    def __init__(self, username: str, uuid: str):
        self.username = username
        self.uuid = uuid

    def get_username(self) -> str:
        return self.username
