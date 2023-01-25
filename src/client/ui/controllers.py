from fastapi import APIRouter, status, Body, Depends
from fastapi.responses import JSONResponse, Response, RedirectResponse
from pydantic import BaseModel, Field
from kink import di
from src.client.domain.repository import ClientRepositoryInterface

router = APIRouter(prefix='/client', tags=['client'])

class ClientRequest(BaseModel):
    name: str
    surname: str
    body: str = Field(min_length=10, max_length=20)


@router.post('create')
async def client_create(client: ClientRequest) -> JSONResponse:
    return client


@router.get('/{client_id}')
async def client_get(
    client_id: int,
    client_repo: ClientRepositoryInterface = Depends(lambda: di[ClientRepositoryInterface])
) -> JSONResponse:
    return {"client": client_repo.get_client(client_id)}
