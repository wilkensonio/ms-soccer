from fastapi import FastAPI
from api.db.database import engine, Base
from api.routes import player  # , club, match

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(player.router, prefix="/players", tags=["Players"])
# app.include_router(club.router, prefix="/clubs", tags=["Clubs"])
# app.include_router(match.router, prefix="/matches", tags=["Matches"])
