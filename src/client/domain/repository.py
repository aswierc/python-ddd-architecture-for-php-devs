from abc import ABC, abstractmethod
from typing import Optional
from src.client.domain.entity import ClientEntity


class ClientRepositoryInterface(ABC):
    @abstractmethod
    def get_client(self, uuid: int) -> Optional[ClientEntity]: ...


    @abstractmethod
    def save(self, entity: ClientEntity) -> None: ...
