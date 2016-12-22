import arcade.key

class Model:
    def __init__(self, world, x, y, angle):
        self.world = world
        self.x = x
        self.y = y
        self.angle = 0

class World:
    def __init__(self,width,height):
        self.width = width
        self.height = height
        self.state = 0
        self.b1 = False
        self.b2 = False
        self.b3 = False
        self.b4 = False
        self.scene_1 = 0
        self.scene_2 = 0
        self.scene_3 = 0
        self.scene_4 = 0
        self.scene_5 = 0

    def state_change(self,key):
        if key == arcade.key.LEFT:
            self.state = self.state + 1
        if key == arcade.key.RIGHT:
            self.state = self.state + 1

    def on_key_press(self,key,key_modifiers):
        if self.state == 0:
            if key == arcade.key.ENTER:
                self.state = 1
        elif self.state != 0:
            self.state_change(key)

        if key == arcade.key.R:
            self.state = 0
            self.b1 = False
            self.b2 = False
            self.b3 = False
            self.b4 = False
            self.scene_1 = 0
            self.scene_2 = 0
            self.scene_3 = 0
            self.scene_4 = 0
            self.scene_5 = 0

    def on_key_release(self,key,key_modifiers):
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            print("123")
