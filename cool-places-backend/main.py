
from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from typing import List, Optional

app = FastAPI()

# Define the base model
Base = declarative_base()

# Define the Location model
class Location(Base):
    __tablename__ = "locations"  # Ensure the table name matches the actual table name in the database

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    description = Column(String(255), nullable=False)

# Create the database engine
engine = create_engine("sqlite:///your_database.db")

# Create the tables
Base.metadata.create_all(bind=engine)

# Create a session
Session = sessionmaker(bind=engine)
db = Session()

# Now you can perform your database operations, such as querying or inserting data
def __init__(self, name, description):
        self.name = name
        self.description = description

class LocationCreate(BaseModel):
    name: str
    description: str

class LocationUpdate(BaseModel):
    name: Optional[str]
    description: Optional[str]

def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()

class LocationResponse(BaseModel):
    id: int
    name: str
    description: str

@app.get("/locations/{location_id}", response_model=LocationResponse)
async def get_location(location_id: int, db: Session = Depends(get_db)):
    location = db.query(Location).filter(Location.id == location_id).first()
    if not location:
        raise HTTPException(status_code=404, detail="Location not found")
    return LocationResponse(id=location.id, name=location.name, description=location.description)

@app.post("/locations", response_model=LocationResponse)
async def create_location(location: LocationCreate, db: Session = Depends(get_db)):
    db_location = Location(name=location.name, description=location.description)
    db.add(db_location)
    db.commit()
    db.refresh(db_location)
    return LocationResponse(id=db_location.id, name=db_location.name, description=db_location.description)

@app.put("/locations/{location_id}", response_model=LocationResponse)
async def update_location(location_id: int, location: LocationUpdate, db: Session = Depends(get_db)):
    db_location = db.query(Location).filter(Location.id == location_id).first()
    if not db_location:
        raise HTTPException(status_code=404, detail="Location not found")
    if location.name:
        db_location.name = location.name
    if location.description:
        db_location.description = location.description
    db.commit()
    db.refresh(db_location)
    return LocationResponse(id=db_location.id, name=db_location.name, description=db_location.description)

@app.delete("/locations/{location_id}")
async def delete_location(location_id: int, db: Session = Depends(get_db)):
    db_location = db.query(Location).filter(Location.id == location_id).first()
    if not db_location:
        raise HTTPException(status_code=404, detail="Location not found")
    db.delete(db_location)
    db.commit()
    return {"message": "Location deleted successfully."}
