from fastapi_events.handlers.local import local_handler
from fastapi_events.typing import Event
from src.client.application.command import CreateClientCommand
from kink import di

from src.client.domain.entity import ClientEntity
from src.client.domain.repository import ClientRepositoryInterface


@local_handler.register(event_name=CreateClientCommand.get_name())
def create_client_handler(event: Event):
    # todo - how to get here payload as CreateClientCommand
    event_name, payload = event

    repo: ClientRepositoryInterface = di[ClientRepositoryInterface]
    repo.save(ClientEntity(payload['user_name'], payload['uuid']))
