import arcade

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
SCREEN_TITLE = "Arcade Game"


class Game(arcade.Window):

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

    def on_draw(self):
        self.clear()

    def on_update(self, delta_time: float):
        pass

window = Game()
arcade.run()

"""
Если в субботу получится, то свяжитесь с Паштетом, чтобы позаниматься

1. ДОСТАТЬ ВСЕ каРТИноЧКИ из плАншеТика (спРайтИки)
2. Добавить двух  персонажа в игрулю и обучить её или его или оно ходить

"""