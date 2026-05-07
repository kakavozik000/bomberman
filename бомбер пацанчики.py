import time
import arcade

SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 720
SCREEN_TITLE = "Arcade Game"



class Boba(arcade.Sprite):

    def __init__(self):
        super().__init__("Bo.png", scale=0.2)
        self.center_x = 1200
        self.center_y = SCREEN_HEIGHT / 3
        self.timer = time.time()
    def update(self):
        if time.time() - self.timer >= 5:
            window.Boa.center_x = self.center_x
            window.Boa.center_y = self.center_y

class Boa(arcade.Sprite):

    def __init__(self):
        super().__init__("Boa.png", scale=1)
        self.center_x = 1200
        self.center_y = SCREEN_HEIGHT / 3
    def update(self):
        if time.time() - self.timer >= 5:
            self.center_x += self.change_x
            self.center_y += self.change_y



class Bobo(arcade.Sprite):

    def __init__(self):
        super().__init__("Bo.png", scale=0.2)
        self.center_x = 1200
        self.center_y = SCREEN_HEIGHT / 3
    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y















class Kambodsha (arcade.Sprite):

    def __init__(self):
        super().__init__('Kam2.png', scale=0.4)
        self.center_x = 1200
        self.center_y = SCREEN_HEIGHT / 3
    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y


class Tailand (arcade.Sprite):

    def __init__(self):
        super().__init__('Tai2.png', scale=0.4)
        self.center_x = 1000
        self.center_y = SCREEN_HEIGHT / 2
    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y






class Game(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE,fullscreen=True)
        self.Kam = Kambodsha()
        self.Tai = Tailand()
        self.set_mouse_visible(False)
        self.fu = arcade.load_texture("Fo.png")
        self.Boba = None
        self.Bobo = None
        self.Boa = Boa()
        self.Boa.center_x = 10000

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.TAB:
            self.close()
        if symbol == arcade.key.RIGHT:
            self.Kam.change_x = 10
        if symbol == arcade.key.LEFT:
            self.Kam.change_x = -10
        if symbol == arcade.key.UP:
            self.Kam.change_y = 10
        if symbol == arcade.key.DOWN:
            self.Kam.change_y = -10
        if symbol == arcade.key.SPACE:
            self.Boba = Boba()
            self.Boba.center_x = self.Kam.center_x
            self.Boba.center_y = self.Kam.center_y

        if symbol == arcade.key.R:
            self.Tai.change_x = 10
        if symbol == arcade.key.L:
            self.Tai.change_x = -10
        if symbol == arcade.key.U:
            self.Tai.change_y = 10
        if symbol == arcade.key.D:
            self.Tai.change_y = -10
        if symbol == arcade.key.F10 :
            self.Bobo = Bobo()
            self.Bobo.center_x = self.Tai.center_x
            self.Bobo.center_y = self.Tai.center_y



    def on_key_release(self, symbol: int, modifiers: int):
        if symbol == arcade.key.RIGHT:
            self.Kam.change_x = 0
        if symbol == arcade.key.LEFT:
            self.Kam.change_x = -0
        if symbol == arcade.key.UP:
            self.Kam.change_y = 0
        if symbol == arcade.key.DOWN:
            self.Kam.change_y = -0

        if symbol == arcade.key.R:
            self.Tai.change_x = 0
        if symbol == arcade.key.L:
            self.Tai.change_x = -0
        if symbol == arcade.key.U:
            self.Tai.change_y = 0
        if symbol == arcade.key.D:
            self.Tai.change_y = -0

    def on_draw(self):
        self.clear()
        arcade.draw_texture_rectangle(self.width / 2, self.height / 2, self.width, self.height,self.fu)
        self.Kam.draw()
        self.Tai.draw()
        arcade.draw_text("Выход = taб,Управление персонажами через стрелочки", 100, 100,
        arcade.color.AMERICAN_ROSE, 30)
        if self.Boba is not None:
            self.Boba.draw()
        if self.Bobo is not None:
            self.Bobo.draw()
        self.Boa.draw()


    def on_update(self, delta_time: float):
        self.Kam.update()
        self.Tai.update()
        if self.Boba is not None:
            self.Boba.update()

window = Game()
arcade.run()

"""
1. Сделать возможность взрываться бомбочке и второого игроку (точно также всё скопировать из первого БОА) оки
2. Картинку "грустного" Тайланда оки
3. Поиграть в БЛ ок
4. лазщэыокушпхыг ага аг,аписываю
5. реагкенгс окей,что дальше?
 картинками (бомбочкеи пропали, попробовать сохранить в другом формате в ибисе)

"""