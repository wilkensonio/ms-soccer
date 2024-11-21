from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from api.db.database import Base


class Player(Base):
    __tablename__ = "players"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(250), index=True)
    age = Column(Integer)
    nationality = Column(String(250))
    position = Column(String(250))
    goals = Column(Integer, default=0)
    assists = Column(Integer, default=0)
    minutes_played = Column(Integer, default=0)
    injuries = Column(Integer, default=0)
    # fan_id = Column(Integer, ForeignKey("fans.id"))
    # club_id = Column(Integer, ForeignKey("clubs.id"))

    # club = relationship("Club", back_populates="players")
    # fan = relationship("Fan", back_populates="players")
