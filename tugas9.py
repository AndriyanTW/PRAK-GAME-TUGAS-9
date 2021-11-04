from direct.showbase.ShowBase import ShowBase

class Myapp(ShowBase):
    def __init__(self):
        super().__init__()
        # Load the environment model.
        self.scene = self.loader.loadModel("models/panda")
        # Reparent the model to render.
        self.scene.reparentTo(self.render)
       # Apply scale and position transforms on the model.
        self.scene.setScale(0.25, 0.25, 0.25)
        self.scene.setPos(-8, 42, 0)

        self.panda = self.loader.load_model("panda.egg.pz")
        self.panda.reparentTo(self.render)
        self.panda.setScale(2, 2, 2)
        self.panda.setPos(-8, 42, 0)


app = Myapp()
app.run()