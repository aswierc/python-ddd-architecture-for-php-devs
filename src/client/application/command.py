import uuid
from datetime import datetime
from enum import Enum
from pydantic import BaseModel
from fastapi_events.registry.payload_schema import registry as payload_schema


class ClientCommands(Enum):
    CREATE = "CLIENT_CREATE"


@payload_schema.register(event_name=ClientCommands.CREATE)
class CreateClientCommand(BaseModel):
    uuid: uuid.UUID
    created_at: datetime
    user_name: str

    @staticmethod
    def get_name() -> str:
        return ClientCommands.CREATE

    @staticmethod
    def create(user_name: str) -> dict:
        return {
            "uuid": uuid.uuid4(),
            "created_at": datetime.utcnow(),
            "user_name": user_name,
        }
