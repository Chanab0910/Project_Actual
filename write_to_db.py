from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from models import Country, Match

# Connect to the activities database
engine = create_engine('sqlite:///World_cup.sqlite3', echo=True)

# Create a session and add the people to the database
with Session(engine) as sess:
    china = Country(Country_name='China', Attack=78, Defense=73, Tier=4)
    sess.add(china)
    # sess.add_all(Match)
    sess.commit()
