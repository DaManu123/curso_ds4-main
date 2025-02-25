from random import choice

from Athlete import Athlete
from Sport import Sport
from Team import Team
from random import choice

class Game:
    '''Class Game: Juego entre dos equipos'''
    sports_dict = {
        'LMP': [x for x in range(0,11)],
        'NBA': [x for x in range(70,121)],
        'NFL': [x for x in range(3, 49)],
        'LMX': [x for x in range(0, 9)],

    }
    def __init__(self, A:Team, B:Team) -> None:
        self.A = A
        self.B = B
        self.score = dict()
        self.score[A.name] = 0
        self.score[B.name] = 0

    def play(self):
        '''Juego simulado entre equipos'''
        league = self.A.sport.league
        points = self.sports_dict[league]
        a = choice(points)
        b = choice(points)
        self.score[self.A.name] = a
        self.score[self.B.name] = b

    def __str__(self) -> str:
        '''Metodo para mostrar clase como string'''
        return f"""Game: {self.A.name:20s}: {self.score[self.A.name]:3d} - {self.score[self.B.name]:3d}: {self.B.name:20s}"""

    def __repr__(self) -> str:
        '''Metodo para representar la clase como string'''
        return f"Game(A={repr(self.A)}, B={repr(self.B)})"

    def to_json(self) -> dict:
        '''Metodo para representar la clase como diccionario'''
        return {"A":self.A.to_json(), "B":self.B.to_json(),"score":self.score}
if __name__ == '__main__':
    dt = ['Jordan','Johnson','Pipen','Bird','Kobe']
    cz = ['Bjovik','Czack','Pfeizer','Leonard','Kempfe']
    players_a = [Athlete(x) for x in dt]
    players_b = [Athlete(x) for x in cz]
    basketball = Sport("DreamTeam",5,"NBA")
    t = Team("Dream Team",basketball,players_a)
    c = Team("Czeck Republic",basketball,players_b)
    game = Game(t, c)
    game.play()
    print(game)
    print(repr(game))
    print("----")
    print(game.to_json())