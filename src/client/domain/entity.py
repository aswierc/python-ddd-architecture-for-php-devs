from typing import Optional

from config.db import Base
from sqlalchemy import Column, String, Integer


class ClientEntity(Base):
    __tablename__ = 'client'
    id: int = Column(Integer, primary_key=True, index=True)
    username: Optional[str] = Column(String)

    def get_username(self) -> str:
        return self.username
