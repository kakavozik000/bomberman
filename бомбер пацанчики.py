import time
import arcade


SCREEN_TITLE = "Бомбермания"
ROW = 8
COLUMN = 16
BLOCK_WIDTH = 100
BLOCK_HEIGHT = 100
SCREEN_WIDTH = COLUMN * BLOCK_WIDTH
SCREEN_HEIGHT = ROW * BLOCK_HEIGHT


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







class Nelomoka (arcade.Sprite):

    def __init__(self):
        super().__init__('блокнет.png', scale=2)







class Kambodsha (arcade.Sprite):

    def __init__(self):
        super().__init__('Kam2.png', scale=0.2)
        self.center_x = 1200
        self.center_y = SCREEN_HEIGHT / 3
    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y


class Tailand (arcade.Sprite):

    def __init__(self):
        super().__init__('Tai2.png', scale=0.25)
        self.center_x = 1000
        self.center_y = SCREEN_HEIGHT / 2
    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y






class Game(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE,fullscreen=False)
        print(self.width, self.height)
        self.Kam = Kambodsha()
        self.Tai = Tailand()
        self.fu = arcade.load_texture("фончпек.png")
        self.bumibut = arcade.SpriteList()
        self.bumibuk = arcade.SpriteList()
        self.ogot = arcade.SpriteList()
        self.ogok = arcade.SpriteList()
        self.bd = arcade.SpriteList()
        self.bn = arcade.SpriteList()

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        kletochka_index_x = x // BLOCK_WIDTH
        kletochka_index_y = y // BLOCK_HEIGHT
        kletochka_center_x = kletochka_index_x * BLOCK_WIDTH + BLOCK_WIDTH // 2
        kletochka_center_y = kletochka_index_y * BLOCK_HEIGHT + BLOCK_HEIGHT // 2

        print(kletochka_index_x,kletochka_index_y,kletochka_center_x,kletochka_center_y)

        pup = Nelomoka()
        pup.center_x = kletochka_center_x
        pup.center_y = kletochka_center_y
        self.bn.append(pup)


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
            self.Tai.change_x = -0
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
        for y in range(ROW):
            for x in range(COLUMN):
                arcade.draw_texture_rectangle(x * BLOCK_WIDTH + BLOCK_WIDTH / 2, y * BLOCK_HEIGHT+BLOCK_HEIGHT/2, BLOCK_WIDTH, BLOCK_HEIGHT,self.fu)
                # arcade.draw_rectangle_outline(x * BLOCK_WIDTH + BLOCK_WIDTH / 2, y * BLOCK_HEIGHT*BLOCK_HEIGHT/2, BLOCK_WIDTH, BLOCK_HEIGHT, color=arcade.color.BLACK)
        self.Kam.draw()
        self.Tai.draw()
        arcade.draw_text("Выход = taб,Управление Фиолетовой чучундрой через стрелочки,рыжей - urld", 100, 100,
        arcade.color.AMERICAN_ROSE, 30)
        arcade.draw_text("у всех по 2 хпхе", 200, 400,
        arcade.color.AMERICAN_ROSE, 30)
        self.bumibut.draw()
        self.bumibuk.draw()
        self.ogot.draw()
        self.ogok.draw()
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

Звуик НЕ СКАЧИВАТЬ БЕЗ ПАШТЕ

1. Узнать как выключить компудатор на питоне, нужен маленький кодик (две строчки) и если его запустить, то
компухтер выключится. Если человек нажало на кномпу ентер, то вырубить ПК
 if symbol == arcade.key.ENTER:
    self.close()

ТА,сделаем это вместе :)) оке
-------------------------------
Погулять
1. По нажатию кнопки - выключать Пк
2. Нам нужны три буста, которые будут лежать на полу (пол рисовать не надо, только сам буст)
Бусты: для скорости, для бомбчек (кол-во их увеличивается), для невидимости, для увеличения кол-во огней
 нарисовать как угодно, например, в виде бутылочек (и  на них там будет нарисовано что-то ) или другой какой-то пример
 
 
 
 
 
  self.fonch = arcade.SpriteList()
  
import  os
os.system("shutdown /s /t 0")
 
 -------------------------
 1. когда мы ставим бомбочку - изменить её размер, чтобы она соответствовала одной клеточке + огонь тоже скейл поменять
 2. сделать так, чтобы игроки не могли выйти за пределы окна (уже делали раньше, подсмотри в прошлые проектики :))
 3. сделать так, чтобы при нажатии на кнопочку ентер - просто выключался компьютер :)
"""