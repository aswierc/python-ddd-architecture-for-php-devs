from pydantic import BaseModel


class CreateClientRequest(BaseModel):
    user_name: str
