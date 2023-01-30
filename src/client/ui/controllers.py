from fastapi import APIRouter, Depends
from fastapi_events.dispatcher import dispatch
from kink import di

from src.client.application.command import CreateClientCommand
from src.client.domain.repository import ClientRepositoryInterface
from src.client.ui.request import CreateClientRequest

router = APIRouter(prefix='/client', tags=['client'])


@router.post('')
async def client_create(
        client: CreateClientRequest
) -> dict:
    command = CreateClientCommand.create(client.user_name)

    dispatch(CreateClientCommand.get_name(), command)

    return {"uuid": command['uuid']}


@router.get('/{client_uuid}')
async def client_get(
        client_uuid: str,
        client_repo: ClientRepositoryInterface = Depends(lambda: di[ClientRepositoryInterface])
) -> dict:
    return {"client": client_repo.get_client(client_uuid)}
