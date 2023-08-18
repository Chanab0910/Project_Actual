from sqlalchemy import Column, Integer, String, Table, UniqueConstraint, ForeignKey, BLOB
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

Base = declarative_base()


class Big_Table_Stats(Base):
    __tablename__ = 'Big_table_stats'
    Country_name = Column(String, primary_key=True, unique=False, nullable=False)
    Attack = Column(Integer, unique=False, nullable=False)
    Defense = Column(Integer, unique=False, nullable=False)
    Tier = Column(Integer, unique=False, nullable=False)
    Goals_scored_in_groups = Column(Integer, unique=False, nullable=False)
    Goals_scored_in_knock_out = Column(Integer, unique=False, nullable=False)
    Games_played_in_group = Column(Integer, unique=False, nullable=False)
    Games_played_in_ko = Column(Integer, unique=False, nullable=False)
    Furthest_stage_got = Column(Integer, unique=False, nullable=False)
    Place_they_got_to_Cumulative = Column(Integer, unique=False, nullable=False)
    Team_beat_most = Column(String, unique=False, nullable=False)
    Number_of_times_beat_highest = Column(Integer, unique=False, nullable=False)
    Team_lost_to_most = Column(String, unique=False, nullable=False)
    Number_of_times_lost_against_highest = Column(Integer, unique=False, nullable=False)
    Most_goals_in_game = Column(Integer, unique=False, nullable=False)
    Most_goals_in_game_team_opposition = Column(String, unique=False, nullable=False)


    def __repr__(self):
        return f"<Big_Table_stats({self.Country_name})>"


class Group1(Base):
    __tablename__ = 'Group1'
    Country_name = Column(Integer, primary_key=True,unique=False, nullable=False )
    Goals_for = Column(Integer,unique=False, nullable=False)
    Goals_against = Column(Integer,unique=False, nullable=False)
    Points = Column(Integer,unique=False, nullable=False)

class Group2(Base):
    __tablename__ = 'Group2'
    Country_name = Column(Integer, primary_key=True, unique=False, nullable=False)
    Goals_for = Column(Integer, unique=False, nullable=False)
    Goals_against = Column(Integer, unique=False, nullable=False)
    Points = Column(Integer, unique=False, nullable=False)

class Group3(Base):
    __tablename__ = 'Group3'
    Country_name = Column(Integer, primary_key=True, unique=False, nullable=False)
    Goals_for = Column(Integer, unique=False, nullable=False)
    Goals_against = Column(Integer, unique=False, nullable=False)
    Points = Column(Integer, unique=False, nullable=False)

class Group4(Base):
    __tablename__ = 'Group4'
    Country_name = Column(Integer, primary_key=True, unique=False, nullable=False)
    Goals_for = Column(Integer, unique=False, nullable=False)
    Goals_against = Column(Integer, unique=False, nullable=False)
    Points = Column(Integer, unique=False, nullable=False)

class Group5(Base):
    __tablename__ = 'Group5'
    Country_name = Column(Integer, primary_key=True,unique=False, nullable=False )
    Goals_for = Column(Integer,unique=False, nullable=False)
    Goals_against = Column(Integer,unique=False, nullable=False)
    Points = Column(Integer,unique=False, nullable=False)

class Group6(Base):
    __tablename__ = 'Group6'
    Country_name = Column(Integer, primary_key=True, unique=False, nullable=False)
    Goals_for = Column(Integer, unique=False, nullable=False)
    Goals_against = Column(Integer, unique=False, nullable=False)
    Points = Column(Integer, unique=False, nullable=False)

class Group7(Base):
    __tablename__ = 'Group7'
    Country_name = Column(Integer, primary_key=True, unique=False, nullable=False)
    Goals_for = Column(Integer, unique=False, nullable=False)
    Goals_against = Column(Integer, unique=False, nullable=False)
    Points = Column(Integer, unique=False, nullable=False)

class Group8(Base):
    __tablename__ = 'Group8'
    Country_name = Column(Integer, primary_key=True, unique=False, nullable=False)
    Goals_for = Column(Integer, unique=False, nullable=False)
    Goals_against = Column(Integer, unique=False, nullable=False)
    Points = Column(Integer, unique=False, nullable=False)