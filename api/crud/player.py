from sqlalchemy.orm import Session
from api.models.player import Player
from api.schemas.player import PlayerCreate


def create_player(db: Session, player: PlayerCreate):
    db_player = Player(**player.dict())
    db.add(db_player)
    db.commit()
    db.refresh(db_player)
    return db_player


def get_player(db: Session, player_id: int):
    return db.query(Player).filter(Player.id == player_id).first()
