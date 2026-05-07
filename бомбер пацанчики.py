import time
import arcade

SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 720
SCREEN_TITLE = "Бомбермания"
ROW = 20
COLUMN =50
BLOCK_WIDTH = 50
BLOCK_HEIGHT = 50



class Boba(arcade.Sprite):

    def __init__(self):
        super().__init__("Bo.png", scale=0.2)
        self.center_x = 1200
        self.center_y = SCREEN_HEIGHT / 3
        self.timer = time.time()
    def update(self):
        if time.time() - self.timer >= 5:
            self.kill()

            boa = Boa()
            boa.center_x = self.center_x
            boa.center_y = self.center_y
            window.ogok.append(boa)


class Boa(arcade.Sprite):

    def __init__(self):
        super().__init__("Boa.png", scale=1)
        self.center_x = 1200
        self.center_y = SCREEN_HEIGHT / 3
        self.timer = time.time()
    def update(self):
        if time.time() - self.timer >= 3:
            self.kill()




class Bobo(arcade.Sprite):

    def __init__(self):
        super().__init__("Bo.png", scale=0.2)
        self.center_x = 1200
        self.center_y = SCREEN_HEIGHT / 3
        self.timer = time.time()
    def update(self):
        if time.time() - self.timer >= 5:
            self.kill()

            boa = Boa()
            boa.center_x = self.center_x
            boa.center_y = self.center_y
            window.ogot.append(boa)















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
        self.bumibut = arcade.SpriteList()
        self.bumibuk = arcade.SpriteList()
        self.ogot = arcade.SpriteList()
        self.ogok = arcade.SpriteList()
        self.fonch = arcade.SpriteList()
        self.bd = arcade.SpriteList()
        self.bn = arcade.SpriteList()


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
            boba = Boba()
            boba.center_x = self.Kam.center_x
            boba.center_y = self.Kam.center_y
            self.bumibuk.append(boba)



        if symbol == arcade.key.R:
            self.Tai.change_x = 10
        if symbol == arcade.key.L:
            self.Tai.change_x = -10
        if symbol == arcade.key.U:
            self.Tai.change_y = 10
        if symbol == arcade.key.D:
            self.Tai.change_y = -10
        if symbol == arcade.key.F10 :
            boba = Boba()
            boba.center_x = self.Tai.center_x
            boba.center_y = self.Tai.center_y
            self.bumibut.append(boba)



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
        self.bumibut.draw()
        self.bumibuk.draw()
        self.ogot.draw()
        self.ogok.draw()
        self.fonch.draw()
        self.bd.draw()
        self.bn.draw()



    def on_update(self, delta_time: float):
        self.Kam.update()
        self.Tai.update()
        self.bumibut.update()
        self.bumibuk.update()
        self.ogot.update()
        self.ogok.update()

window = Game()
arcade.run()

"""
1. Узнать как выключить компудатор на питоне, нужен маленький кодик (две строчки) и если его запустить, то
компухтер выключится. Если человек нажало на кномпу ентер, то вырубить ПК

2. В окне просто отрисовать несколько надписей (хпшки первого игрока и второого)
3. Погулять сегодня
4. Найти звуки для взрыва и можно на задний фон (по желанию), звуки ходьбы (по желнию)
Звуик НЕ СКАЧИВАТЬ БЕЗ ПАШТЕТА,сделаем это вместе :))
"""