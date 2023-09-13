from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from models import Country, Match
import random

# Connect to the activities database
engine = create_engine('sqlite:///World_cup.sqlite3', echo=True)

sess = Session(engine)
tier1 = []
count = 0

country = sess.query(Country).first()
countries = sess.query(Country).all()
tier1_countries = sess.query(Country).filter_by(Tier = 1).all()
china = sess.query(Country).filter_by(Country_name='China').first()

for i in range(8):
    random_country = random.choice(countries)
