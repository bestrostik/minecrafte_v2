from direct.showbase.ShowBase import ShowBase
from map import Map

class Game(ShowBase):
    def __init__(self):
        super().__init__(self)
        self.map = Map()

base = Game()



base.run()