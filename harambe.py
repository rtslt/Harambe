import arcade
import random
from models import World
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

class ModelSprite(arcade.Sprite):
    def __init__(self, *args, **kwargs):
        self.model = kwargs.pop('model', None)

        super().__init__(*args, **kwargs)

    def sync_with_model(self):
        if self.model:
            self.set_position(self.model.x, self.model.y)
            self.angle = self.model.angle

    def draw(self):
        self.sync_with_model()
        super().draw()
################################################################################
class GameWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)
        arcade.set_background_color(arcade.color.BLACK)

        self.L = [1,2,3,4,5]

        self.world = World(width,height)
        self.i = -1
        self.i2 = -1
        self.i3 = -1
        self.i4 = -1
        self.i5 = -1

        self.bg_sprite = ModelSprite('images/harambe.png')
        self.bg_sprite.set_position(300,300)

        self.scene_1 = ModelSprite('images/decision_1.png')
        self.scene_1.set_position(300,300)

        self.scene_2 = ModelSprite('images/decision_2.png')
        self.scene_2.set_position(300,300)

        self.scene_3 = ModelSprite('images/decision_3.png')
        self.scene_3.set_position(300,300)

        self.scene_4 = ModelSprite('images/decision_4.png')
        self.scene_4.set_position(300,300)

        self.scene_5 = ModelSprite('images/decision_5.png')
        self.scene_5.set_position(300,300)
################################################################################
    def on_draw(self):
        arcade.start_render()
        if self.world.state == 0:
            self.L = [1,2,3,4,5]
            self.bg_sprite.draw()
            arcade.draw_text("Press Enter key to start", 5, 10, arcade.color.WHITE, 30)
################################################################################
        elif self.world.state == 1:
            self.get_random()
            if self.i == 1:
                self.scene_1.draw()
            elif self.i == 2:
                self.scene_2.draw()
            elif self.i == 3:
                self.scene_3.draw()
            elif self.i == 4:
                self.scene_4.draw()
            elif self.i == 5:
                self.scene_5.draw()
################################################################################
        elif self.world.state == 2:
            self.get_random()
            if self.i2 == 1:
                self.scene_1.draw()
            elif self.i2 == 2:
                self.scene_2.draw()
            elif self.i2 == 3:
                self.scene_3.draw()
            elif self.i2 == 4:
                self.scene_4.draw()
            elif self.i2 == 5:
                self.scene_5.draw()
################################################################################
        elif self.world.state == 3:
            self.get_random()
            if self.i3 == 1:
                self.scene_1.draw()
            elif self.i3 == 2:
                self.scene_2.draw()
            elif self.i3 == 3:
                self.scene_3.draw()
            elif self.i3 == 4:
                self.scene_4.draw()
            elif self.i3 == 5:
                self.scene_5.draw()
################################################################################
        elif self.world.state == 4:
            self.get_random()
            if self.i4 == 1:
                self.scene_1.draw()
            elif self.i4 == 2:
                self.scene_2.draw()
            elif self.i4 == 3:
                self.scene_3.draw()
            elif self.i4 == 4:
                self.scene_4.draw()
            elif self.i4 == 5:
                self.scene_5.draw()
################################################################################
        elif self.world.state == 5:
            self.get_random()
            if self.i5 == 1:
                self.scene_1.draw()
            elif self.i5 == 2:
                self.scene_2.draw()
            elif self.i5 == 3:
                self.scene_3.draw()
            elif self.i5 == 4:
                self.scene_4.draw()
            elif self.i5 == 5:
                self.scene_5.draw()
################################################################################

################################################################################
    def get_random(self):
        if self.world.b1 == False and self.world.state == 1:
            self.i = random.choice(self.L)
            self.world.b1 = True
            self.L.remove(self.i)

        elif self.world.b2 == False and self.world.state == 2:
            self.i2 = random.choice(self.L)
            self.world.b2 = True
            self.L.remove(self.i2)

        elif self.world.b3 == False and self.world.state == 3:
            self.i3 = random.choice(self.L)
            self.world.b3 = True
            self.L.remove(self.i3)

        elif self.world.b4 == False and self.world.state == 4:
            self.i4 = random.choice(self.L)
            self.world.b4 = True
            self.L.remove(self.i4)
        elif self.world.state == 5:
            self.i5 = self.L[0]
################################################################################
    def on_key_press(self, key, key_modifiers):
        #Left is -1
        if self.world.state == 1:
            if key == arcade.key.LEFT:
                self.world.scene_1 = -1
            if key == arcade.key.RIGHT:
                self.world.scene_1 = 1
        if self.world.state == 2:
            if key == arcade.key.LEFT:
                self.world.scene_2 = -1
            if key == arcade.key.RIGHT:
                self.world.scene_2 = 1
        if self.world.state == 3:
            if key == arcade.key.LEFT:
                self.world.scene_3 = -1
            if key == arcade.key.RIGHT:
                self.world.scene_3 = 1
        if self.world.state == 4:
            if key == arcade.key.LEFT:
                self.world.scene_3 = -1
            if key == arcade.key.RIGHT:
                self.world.scene_3 = 1
        if self.world.state == 5:
            if key == arcade.key.LEFT:
                self.world.scene_3 = -1
            if key == arcade.key.RIGHT:
                self.world.scene_3 = 1
        self.world.on_key_press(key, key_modifiers)

    def on_key_release(self, key, key_modifiers):
        self.world.on_key_release(key, key_modifiers)

if __name__ == '__main__':
    window = GameWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()
