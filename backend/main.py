from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import Annotated
import models
from database import engine, SessionLocale
from sqlalchemy.orm import Session

app = FastAPI()
models.Base.metadata.create_all(bind=engine)


class PlanetBase(BaseModel):
    name: str
    type: str
    moonCount: int

class SystemBase(BaseModel):
    name: str
    galaxy: str
    planetCount: int


def get_db():
    db = SessionLocale()
    try:
        yield db
    finally:
        db.close()
    

db_dependecy = Annotated[Session, Depends(get_db)]

@app.get("/")
async def root():
    return {"message": "Hello world! this is the starboy API"}

#system routes
@app.post("/systems")
async def add_system(system: SystemBase, db: db_dependecy):
    db_system = models.Systems(name=system.name, galaxy=system.galaxy)
    db.add(db_system)
    db.commit()

@app.get("/systems/{system_id}")
async def get_system(system_id: int, db: db_dependecy):
    res = db.query(models.Systems).filter(models.Systems.id == system_id).first()
    if not res:
        raise HTTPException(status_code=404, detail='System not found')
    return res

@app.get("/systems")
async def get_all_systems(db: db_dependecy):
    res = db.query(models.Systems).all()
    if not res:
        raise HTTPException(status_code=404, detail='No systems found')
    return res

#planet routes
@app.post("/planets/{system_id}")
async def add_planet(system_id: int, planet: PlanetBase, db: db_dependecy):
    db_system = db.query(models.Systems).filter(models.Systems.id == system_id).first()
    if not db_system:
        raise HTTPException(status_code=404, detail='System not found')

    db_planet = models.Planets(name=planet.name, type=planet.type, moonCount=planet.moonCount, system_id=system_id)
    db.add(db_planet)

    db_system.planetCount += 1

    db.commit()
    db.refresh(db_system)

    return {"system planet count": db_system.planetCount}

@app.get("/planets/{system_id}")
async def get_planets_in_system(system_id: int, db: db_dependecy):
    res = db.query(models.Planets).filter(models.Planets.system_id == system_id).all()
    if not res:
        raise HTTPException(status_code=404, detail='Planets not found')
    return res