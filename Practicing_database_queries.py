import sqlite3

conn = sqlite3.connect("World_cup.sqlite3")
cursor = conn.cursor()
group1= []
Create_tier_2 = """
SELECT Country_name FROM Country
"""


cursor.execute(Create_tier_2)
for item in cursor.fetchall():
    group1.append(item)
conn.commit()
conn.close()
print(group1[0])


class create_group:
    def __init__(self):

