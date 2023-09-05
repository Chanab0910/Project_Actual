from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from models import Country, Match



# Connect to the activities database
engine = create_engine('sqlite:///World_cup.sqlite3', echo=True)

# Create a session and add the people to the database
with Session(engine) as sess:
    sess.add_all(Country)
    sess.add_all(Match)
    sess.commit()