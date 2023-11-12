class Map():
    def __init__(self):
        self.block_sours = 'sours/block.egg'
        self.texture_sours = 'sours/stone.png'
        self.add_stic()
        for x in range(15):
            for y in range(10):          
                self.add_block((x,0,y))

    def add_block(self,pos):
        self.model = loader.loadModel(self.block_sours)
        self.texture = loader.loadTexture(self.texture_sours)
        self.model.setTexture(self.texture)
        self.model.setPos(pos)
        # self.model.reparentTo(render)
        self.model.reparentTo(self.stic)
    
    def add_stic(self):
        self.stic = render.attachNewNode('sticN1')
