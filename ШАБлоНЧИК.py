import random
import time

import arcade

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
SCREEN_TITLE = "star wars"


class Kek(arcade.Sprite):
    def __init__(self):
        super().__init__(r'C:\Users\user\PyCharmMiscProject\стрелялкa.png', scale=0.4)
        self.center_x = SCREEN_WIDTH / 5
        self.center_y = SCREEN_HEIGHT / 3



class Lela(arcade.Sprite):
    def __init__(self):
        super().__init__('Ляля.png', scale=0.4)
        self.center_x = 1500
        self.center_y = SCREEN_HEIGHT / 3
        self.change_x = -7.5
        self.hp = 10
    def update(self):
        self.center_x += self.change_x
        if self.hp <= 0:
            self.kill()
        if self.right < 0:
            self.left = 1707



class Kolya(arcade.Sprite):
    def __init__(self):
        super().__init__('коленька.png', scale=0.2)
        self.center_x = 1500
        self.center_y = SCREEN_HEIGHT / 3
        self.change_x = -7.5
        self.hp = 10
    def update(self):
        self.center_x += self.change_x
        if self.hp <= 0:
            self.kill()
        if self.right < 0:
            self.left = 1707

class Lazer (arcade.Sprite):

    def __init__(self):
        super().__init__('лазеры.png', scale=1)
        self.center_x = 1500
        self.center_y = SCREEN_HEIGHT / 3
        self.change_x = 15
    def update(self):
        self.center_x += self.change_x
        if self.left >1000:
            self.kill()



class Mihail(arcade.Sprite):

    def __init__(self):
        super().__init__('Михаил.png', scale=0.4)
        self.center_x = 1500
        self.center_y = SCREEN_HEIGHT / 3
        self.change_x = -7.5
        self.hp = 15
    def update(self):
        self.center_x += self.change_x
        if self.hp <= 0:
            self.kill()
        if self.right <0:
            self.left = 1707
class Game(arcade.Window):



    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, fullscreen=True)
        self.Sam = Kek()
        self.seka = 60
        self.set_mouse_visible(False)
        self.lyalya = arcade.load_texture("фон.jpeg")
        self.pipi = False
        self.Mi = Mihail()
        self.Le = Lela()
        self.piupiu = arcade.load_sound("piupiu.mp3")
        self.Ko = Kolya()
        self.warechki = arcade.SpriteList()
        self.lazeri = arcade.SpriteList()
        self.kulya = time.time()
        self.tama = time.time()
        self.sost = True
        self.wui = True



        for w in range (250):
            susu = random.randint(0,2)
            if susu == 0:
                pis = Mihail()
            elif susu == 1:
                pis = Kolya()
            elif susu == 2:
                pis = Lela()
            pis.center_y = random.randint(0, self.height)
            pis.center_x = 500 + w * 60
            self.warechki.append(pis)





    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        if self.sost == True:
            self.Sam.center_y = y



    def on_draw(self):
        self.clear()
        arcade.draw_texture_rectangle(self.width / 2, self.height / 2, self.width, self.height, self.lyalya)
        self.lazeri.draw()
        self.Sam.draw()
        self.Ko.draw()
        self.Le.draw()
        self.Mi.draw()
        self.warechki.draw()
       arcade.draw_text(f"осталось {int(self.tama + self.seka - time.time())} секунд на истребление",100,100,arcade.color.AMERICAN_ROSE,30)
        if self.sost == False:
            if self.wui == False:
                arcade.draw_text("ТЫ ПРОИГРАЛ МУААХАХАХХАХАХАХА", 600, 800,arcade.color.COOL_BLACK, 30)
            if self.wui == True:
                arcade.draw_text("ТЫ ВЫИГРАЛ!:3", 600, 800,arcade.color.COOL_BLACK, 30)
    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.TAB:
            self.close()

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        if self.sost == True:
            if time.time() - self.kulya > 0:
                self.kulya = time.time()
                caca = Lazer()
                caca.center_x = self.Sam.center_x
                caca.center_y = self.Sam.center_y
                self.lazeri.append(caca)
                self.pipi = True
                arcade.play_sound(self.piupiu, volume=0.3)
    def on_mouse_release(self, x: int, y: int, button: int, modifiers: int):
        self.pipi = False
    def on_update(self, delta_time: float):
        if (self.tama + self.seka - time.time()) < 0:
            self.sost = False
            if len( self.warechki)>0:
                self.wui = False


        if self.sost == True:
            self.warechki.update()
            self.lazeri.update()
            if self.pipi and time.time() - self.kulya > 0:
                self.kulya = time.time()

                caca = Lazer()
                caca.center_x = self.Sam.center_x
                caca.center_y = self.Sam.center_y
                self.lazeri.append(caca)
                arcade.play_sound(self.piupiu,volume=0.3)
            for gugu in self.lazeri:
                hihihaha = arcade.check_for_collision_with_list(gugu, self.warechki)
                if  len (hihihaha)>0:
                    gugu.kill()
                    for varechek in hihihaha:
                        varechek.hp -=1
            if len(self.warechki) == 0 :
                self.sost = False



window = Game()
arcade.run()

