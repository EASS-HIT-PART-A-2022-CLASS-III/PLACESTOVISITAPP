from main import app
from fastapi import FastAPI, Depends
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.orm import declarative_base
from typing import Optional

app = FastAPI()

# Database connection
DATABASE_URL = "sqlite:///./database.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Database models
class Location(Base):
    __tablename__ = "locations"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)

    def __init__(self, name, country, description):
        self.name = name
        self.country = country
        self.description = description

class LocationCreate(BaseModel):
    name: str
    country: str
    description: str

class LocationUpdate(BaseModel):
    name: Optional[str]
    country: Optional[str]
    description: Optional[str]

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/locations")
async def create_location(location: LocationCreate, db: Session = Depends(get_db)):
    # create a new location in the DB
    return {"id": 1, **location.dict()}


@app.get("/locations/{location_id}")
async def read_location(location_id: int):
    # retrieve a location from the DB and return it
    return {
        "id": location_id,
        "name": "Camp nou",
        "country": "Spain",
        "description": "Barcelona cool football stadium",
    }       

@app.put("/locations/{location_id}")
async def update_location(location_id: int, location: LocationUpdate):
    # update some location in the DB and return it
    return {"id": location_id, **location.dict()}

@app.delete("/locations/{location_id}")
async def delete_location(location_id: int):
    # delete a location from DB
    return {"message": "Location deleted successfully."}
