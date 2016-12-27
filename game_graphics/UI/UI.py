import game_graphics.UI.Resource_Bar
import World
import KeyListener

class UI:
    def __init__(self):
        self.state = "Game_state"
        self.menu = None
        self.resource_bar = game_graphics.UI.Resource_Bar.Reasource_Bar()
        self.player_info_bar = None
        self.current_bar = None

    def update(self):
        if self.state == "Game_state":
            if World.World.tiles_hash[(World.World.camera_y + KeyListener.mouseY) >> 5][(World.World.camera_x + KeyListener.mouseX) >> 5].building != None:

                self.current_bar = World.World.tiles_hash[(World.World.camera_y + KeyListener.mouseY) >> 5][(World.World.camera_x + KeyListener.mouseX) >> 5].building


    def render(self, display):
        self.resource_bar.render(display)
        if self.current_bar != None:
             self.current_bar.render(display)

    def get_state(self):
        pass