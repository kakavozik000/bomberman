import arcade

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
SCREEN_TITLE = "Arcade Game"

class Kambodsha (arcade.Sprite):

    def __init__(self):
        super().__init__('Kamb1.png', scale=0.4)
        self.center_x = 1500
        self.center_y = SCREEN_HEIGHT / 3


class Tailand (arcade.Sprite):

    def __init__(self):
        super().__init__('Tai1.png', scale=0.4)
        self.center_x = 1400
        self.center_y = SCREEN_HEIGHT / 3






class Game(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        self.kam = Kambodsha()
        self.Tai = Tailand()
        self.set_mouse_visible(False)

def on_key_press(self, symbol: int, modifiers: int):
    if symbol == arcade.key.TAB:
        self.close()

    def on_draw(self):
        self.clear()
        arcade.draw_texture_rectangle(self.width / 2, self.height / 2, self.width, self.height)
        self.Kam.draw()
        self.Tai.draw()
        arcade.draw_text("Выход = taб,Управление персонажами через стрелочки", 100, 100,
        arcade.color.AMERICAN_ROSE, 30)

    def on_update(self, delta_time: float):
        pass

window = Game()
arcade.run()

"""
Если в субботу получится, то свяжитесь с Паштетом, чтобы позаниматься yt gjkexbnwf:(

1. ДОСТАТЬ ВСЕ каРТИноЧКвевИ из плАншеТа (спРайтИки) полушилось 
2. Добавить двух  персонажа в игрулю и обучить её  или оно ходит е умеет,но я смошла отрисовать

"""