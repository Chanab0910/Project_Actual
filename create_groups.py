import read_from_db
from random import randint, shuffle, sample

group1 = []
group2 = []
group3 = []
group4 = []
group5 = []
group6 = []
group7 = []
group8 = []

groups = []
# create list of objects
# don't have lots of variables with 1 parameter changed

countries_in_tiers = []

countries_in_tiers.append(sample(read_from_db.tier1_countries, len(read_from_db.tier1_countries)))
countries_in_tiers.append(sample(read_from_db.tier2_countries, len(read_from_db.tier2_countries)))
countries_in_tiers.append(sample(read_from_db.tier3_countries, len(read_from_db.tier3_countries)))
countries_in_tiers.append(sample(read_from_db.tier4_countries, len(read_from_db.tier4_countries)))

#for group, country in zip([group8, group7, group6, group5, group4, group3, group2, group1], tier1):
#    group.append(country)

#for group, country in zip([group8, group7, group6, group5, group4, group3, group2, group1], tier2):
 #   group.append(country)

#for group, country in zip([group8, group7, group6, group5, group4, group3, group2, group1], tier3):
 #   group.append(country)

#for group, country in zip([group8, group7, group6, group5, group4, group3, group2, group1], tier4):
 #   group.append(country)
