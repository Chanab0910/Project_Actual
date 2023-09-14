import sqlite3

conn = sqlite3.connect("World_cup.sqlite3")
cursor = conn.cursor()
group1= []
Create_tier_2 = """
UPDATE Country
SET Tier = 2
WHERE Tier != 1;

"""


cursor.execute(Create_tier_2)
conn.commit()
conn.close()