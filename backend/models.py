from sqlalchemy import Column, ForeignKey, Integer, String
from database import Base

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
    