from sqlalchemy import create_engine
from sqlalchemy.orm import Session

import create_groups


class simulate_group:

    def __init__(self):
        self.current_group = ''
        self.count = 0
        self.groups = [self.group1, self.group2, self.group2, self.group3, self.group4, self.group5, self.group6,
                       self.group7, self.group8]
        self.group1 = create_groups.group1
        self.group2 = create_groups.group2
        self.group3 = create_groups.group3
        self.group4 = create_groups.group4
        self.group5 = create_groups.group5
        self.group6 = create_groups.group6
        self.group7 = create_groups.group7
        self.group8 = create_groups.group8

        self.engine = create_engine('sqlite:///World_cup.sqlite3', echo=True)
        self.sess = Session(self.engine)

    def choose_which_group(self):
        self.current_group = self.groups[self.count]
        print(self.current_group)
        return self.current_group

    def order_of_play(self):
        self.match(self.current_group, 1)
        self.match(self.current_group, 2)
        self.match(self.current_group, 3)
        self.match(self.current_group, 4)
        self.match(self.current_group, 5)
        self.match(self.current_group, 6)
        self.match(self.current_group, 7)

    def match(self, group, game):
        with Session(self.engine) as self.sess:
            self.Game = Match(Home_team= )



print(simulate_group.choose_which_group)
