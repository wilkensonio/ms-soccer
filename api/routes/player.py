from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from api.crud.player import create_player, get_player
from api.db.database import get_db
from api.schemas.player import Player, PlayerCreate

router = APIRouter()


@router.post("/", response_model=Player)
def create_new_player(player: PlayerCreate, db: Session = Depends(get_db)):
    return create_player(db, player)


@router.get("/{player_id}", response_model=Player)
def read_player(player_id: int, db: Session = Depends(get_db)):
    db_player = get_player(db, player_id)
    if not db_player:
        raise HTTPException(status_code=404, detail="Player not found")
    return db_player
