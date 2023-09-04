from sqlalchemy import Column, Integer, String, Table, UniqueConstraint, ForeignKey, BLOB
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

Base = declarative_base()


class Country(Base):
    __tablename__ = 'Country'
    Country_name = Column(String, primary_key=True, unique=False, nullable=False)
    Attack = Column(Integer, unique=False, nullable=False)
    Defense = Column(Integer, unique=False, nullable=False)
    Tier = Column(Integer, unique=False, nullable=False)




class Match(Base):
    __tablename__ = 'Match'
    Home_team = Column(String, primary_key=True, unique=False, nullable=False)
    Away_team = Column(String, primary_key=True, unique=False, nullable=False)
    Stage = Column(Integer, unique=False, nullable=False)
    Home_goals = Column(Integer, unique=False, nullable=False)
    Away_goals = Column(Integer, unique=False, nullable=False)
    Winner = Column(String, unique=False, nullable=False)

