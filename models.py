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
        self.scene_1 = -1
        self.scene_2 = -1
        self.scene_3 = -1
        self.scene_4 = -1
        self.scene_5 = -1
        self.page_1 = -1
        self.page_2 = -1
        self.page_3 = -1
        self.page_4 = -1
        self.page_5 = -1

    def check_page(self,scene,state):
        if state == 1:
            if scene == 1:
                self.page_1 = self.scene_1
            elif scene == 2:
                self.page_2 = self.scene_1
            elif scene == 3:
                self.page_3 = self.scene_1
            elif scene == 4:
                self.page_4 = self.scene_1
            elif scene == 5:
                self.page_5 = self.scene_1

        elif state == 2:
            if scene == 1:
                self.page_1 = self.scene_2
            elif scene == 2:
                self.page_2 = self.scene_2
            elif scene == 3:
                self.page_3 = self.scene_2
            elif scene == 4:
                self.page_4 = self.scene_2
            elif scene == 5:
                self.page_5 = self.scene_2

        elif state == 3:
            if scene == 1:
                self.page_1 = self.scene_3
            elif scene == 2:
                self.page_2 = self.scene_3
            elif scene == 3:
                self.page_3 = self.scene_3
            elif scene == 4:
                self.page_4 = self.scene_3
            elif scene == 5:
                self.page_5 = self.scene_3

        elif state == 4:
            if scene == 1:
                self.page_1 = self.scene_4
            elif scene == 2:
                self.page_2 = self.scene_4
            elif scene == 3:
                self.page_3 = self.scene_4
            elif scene == 4:
                self.page_4 = self.scene_4
            elif scene == 5:
                self.page_5 = self.scene_4

        elif state == 5:
            if scene == 1:
                self.page_1 = self.scene_5
            elif scene == 2:
                self.page_2 = self.scene_5
            elif scene == 3:
                self.page_3 = self.scene_5
            elif scene == 4:
                self.page_4 = self.scene_5
            elif scene == 5:
                self.page_5 = self.scene_5

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
            self.scene_1 = -1
            self.scene_2 = -1
            self.scene_3 = -1
            self.scene_4 = -1
            self.scene_5 = -1
            self.page_1 = -1
            self.page_2 = -1
            self.page_3 = -1
            self.page_4 = -1
            self.page_5 = -1

    def on_key_release(self,key,key_modifiers):
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            print("123")
