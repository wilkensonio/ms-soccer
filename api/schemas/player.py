
from pydantic import BaseModel


class PlayerBase(BaseModel):
    name: str
    age: int
    nationality: str
    position: str
    goals: int = 0
    assists: int = 0
    minutes_played: int = 0
    injuries: int = 0


class PlayerCreate(PlayerBase):
    pass


class Player(PlayerBase):
    id: int
    fan_id: int
    club_id: int

    class Config:
        orm_mode = True
