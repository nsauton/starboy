from sqlalchemy import Column, ForeignKey, Integer, String, Float
from database import Base

class Stars(Base):
    __tablename__ = 'stars'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, default='')
    constellation = Column(String, index=True, default='')
    rightAscension = Column(Float)
    declination = Column(Float)
    visualMagnitude = Column(Float)
    temperature = Column(Integer)
    spectralType = Column(String, default='')
    description = Column(String, default='')

class Systems(Base):
    __tablename__ = 'systems'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True) 
    planetCount = Column(Integer, default=0)
    galaxy = Column(String)
    

class Planets(Base):
    __tablename__ = 'planets'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    type = Column(String)
    moonCount = Column(Integer, default=0)
    system_id = Column(Integer, ForeignKey("systems.id"))

#could add moon and galaxy tables in the future
    