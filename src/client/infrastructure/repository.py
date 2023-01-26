from typing import Optional
from sqlalchemy.orm import Session
from src.client.domain.entity import ClientEntity
from src.client.domain.repository import ClientRepositoryInterface


class ClientRepository(ClientRepositoryInterface):
    def __init__(self, db):
        self._db: Session = db

    def get_client(self, uuid: int) -> Optional[ClientEntity]:
        entity: Optional[ClientEntity] = self._db\
            .query(ClientEntity)\
            .filter(ClientEntity.uuid == uuid)\
            .one()

        if entity is None:
            return None

        return entity

    def save(self, entity: ClientEntity) -> None:
        self._db.add(entity)
        self._db.commit()
