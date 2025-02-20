
from Athlete import Athlete
from Sport import Sport
class Team:

    def __init__(self, name:str, sport:Sport, players:list):

        self.name = name
        self.sport = sport
        self.players = players

    def __str__(self):

        return f"Team {self.name}, {self.sport}, {self.players}"

    def __repr__(self):

        return f"Team='{self.name}', {self.sport}, {self.players}"

    def to_json(self)->dict:

        return {"name": self.name, "sport": self.sport.to_json(), "players": [p.to_json() for p in self.players]}

if __name__ == "__main__":
    a1 = Athlete("Michael Jordan")
    a2 = Athlete("Kobe Bryant")
    a3 = Athlete("LeBron James")
    a4 = Athlete("Magic Johnson")
    a5 = Athlete("Shaquille O'Neal")
    s = Sport("Basketball", 5, "NBA")
    lakers = Team("Los Angeles Lakers", s, [a1,a2,a3,a4,a5])
    print(lakers)
    print(repr(lakers))