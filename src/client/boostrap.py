from kink import di
from src.client.domain.repository import ClientRepositoryInterface
from src.client.infrastructure.repository import ClientRepository
from config.db import get_db


def bootstrap_di() -> None:
    di[ClientRepositoryInterface] = ClientRepository(get_db())
