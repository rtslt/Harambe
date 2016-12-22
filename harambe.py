import arcade
import random
import msvcrt as m
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

        self.end_0 = ModelSprite('images/end_00000.png')
        self.end_0.set_position(300,300)

        self.end_1 = ModelSprite('images/end_00001.png')
        self.end_1.set_position(300,300)

        self.end_2 = ModelSprite('images/end_00010.png')
        self.end_2.set_position(300,300)

        self.end_3 = ModelSprite('images/end_00011.png')
        self.end_3.set_position(300,300)

        self.end_4 = ModelSprite('images/end_00100.png')
        self.end_4.set_position(300,300)

        self.end_5 = ModelSprite('images/end_00101.png')
        self.end_5.set_position(300,300)

        self.end_6 = ModelSprite('images/end_00110.png')
        self.end_6.set_position(300,300)

        self.end_7 = ModelSprite('images/end_00111.png')
        self.end_7.set_position(300,300)

        self.end_8 = ModelSprite('images/end_01000.png')
        self.end_8.set_position(300,300)

        self.end_9 = ModelSprite('images/end_01001.png')
        self.end_9.set_position(300,300)
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
        else :
            a = (self.world.page_1*16) + (self.world.page_2*8) + (self.world.page_3*4) + (self.world.page_4*2) + (self.world.page_5*1)
            if a == 0 or a == 12 or a == 14:
                self.end_0.draw()
            if a == 1 or a == 25 or a == 27:
                self.end_1.draw()
            if a == 2 or a == 18 or a == 26 or a == 30:
                self.end_2.draw()
            if a == 3 or a == 19 or a == 31:
                self.end_3.draw()
            if a == 4 or a == 20 or a == 28:
                self.end_4.draw()
            if a == 5 or a == 17 or a == 29:
                self.end_5.draw()
            if a == 6 or a == 10 or a == 22:
                self.end_6.draw()
            if a == 7 or a == 21 or a == 23:
                self.end_7.draw()
            if a == 8 or a == 16 or a == 24:
                self.end_8.draw()
            if a == 9 or a == 15 or a == 11 or a== 13:
                self.end_9.draw()
            arcade.draw_text("Press R key to restart", 400, 10, arcade.color.WHITE, 15)
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
        #Left is 0
        if self.world.state == 1:
            if key == arcade.key.LEFT:
                self.world.scene_1 = 0
                self.world.check_page(self.i,1)
            if key == arcade.key.RIGHT:
                self.world.scene_1 = 1
                self.world.check_page(self.i,1)
        if self.world.state == 2:
            if key == arcade.key.LEFT:
                self.world.scene_2 = 0
                self.world.check_page(self.i2,2)
            if key == arcade.key.RIGHT:
                self.world.scene_2 = 1
                self.world.check_page(self.i2,2)
        if self.world.state == 3:
            if key == arcade.key.LEFT:
                self.world.scene_3 = 0
                self.world.check_page(self.i3,3)
            if key == arcade.key.RIGHT:
                self.world.scene_3 = 1
                self.world.check_page(self.i3,3)
        if self.world.state == 4:
            if key == arcade.key.LEFT:
                self.world.scene_4 = 0
                self.world.check_page(self.i4,4)
            if key == arcade.key.RIGHT:
                self.world.scene_4 = 1
                self.world.check_page(self.i4,4)
        if self.world.state == 5:
            if key == arcade.key.LEFT:
                self.world.scene_5 = 0
                self.world.check_page(self.i5,5)
            if key == arcade.key.RIGHT:
                self.world.scene_5 = 1
                self.world.check_page(self.i5,5)
        self.world.on_key_press(key, key_modifiers)
        self.print_boolean()

    def print_boolean(self):
        print('state ',self.world.state)
        print('scene1 ',self.world.scene_1,' page ',self.world.page_1)
        print('scene2 ',self.world.scene_2,' page ',self.world.page_2)
        print('scene3 ',self.world.scene_3,' page ',self.world.page_3)
        print('scene4 ',self.world.scene_4,' page ',self.world.page_4)
        print('scene5 ',self.world.scene_5,' page ',self.world.page_5)

    def on_key_release(self, key, key_modifiers):
        self.world.on_key_release(key, key_modifiers)

    def wait(self):
        m.getch()

    def set_answer(self,scene,state):
        if state == 1:
            a = self.world.scene_1 == -1
        elif state == 2:
            a = self.world.scene_2 == -1
        elif state == 3:
            a = self.world.scene_3 == -1
        elif state == 4:
            a = self.world.scene_4 == -1
        elif state == 5:
            a = self.world.scene_5 == -1

        if scene == self.scene_1:
            #self.wait()
            self.world.page_1 = self.world.scene_1
        if scene == self.scene_2:
            #self.wait()
            self.world.page_2 = self.world.scene_2
        if scene == self.scene_3:
            #self.wait()
            self.world.page_3 = self.world.scene_3
        if scene == self.scene_4:
            #self.wait()
            self.world.page_4 = self.world.scene_4
        if scene == self.scene_5:
            #self.wait()
            self.world.page_5 = self.world.scene_5

if __name__ == '__main__':
    window = GameWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()
