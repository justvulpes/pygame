import game_graphics.UI.Resource_Bar
import game_graphics.UI.Player_Info_Bar
import game_graphics.UI.Weapon_Info
import World
import KeyListener


class UI:

    user_interface_font = "IrisUPC"
    user_interface_font_size = 22

    def __init__(self):
        self.state = "Game_state"
        self.menu = None
        self.resource_bar = game_graphics.UI.Resource_Bar.ResourceBar()
        self.player_info_bar = game_graphics.UI.Player_Info_Bar.PlayerInfoBar()
        self.weapon_info = game_graphics.UI.Weapon_Info.WeaponInfo()
        self.current_bar = None

    def update(self):
        if self.state == "Game_state":
            if 0 <= int(World.World.camera_y + KeyListener.mouseY) >> 5 < World.World.map_height and 0 <= int(World.World.camera_x + KeyListener.mouseX) >> 5 < World.World.map_width:
                if World.World.tiles_hash[(World.World.camera_y + KeyListener.mouseY) >> 5][(World.World.camera_x + KeyListener.mouseX) >> 5].building is not None:
                    self.current_bar = World.World.tiles_hash[(World.World.camera_y + KeyListener.mouseY) >> 5][(World.World.camera_x + KeyListener.mouseX) >> 5].building

    def render(self, display):
        self.resource_bar.render(display)
        self.player_info_bar.render(display)
        self.weapon_info.render(display)

        if self.current_bar is not None:
             self.current_bar.render(display)

    def get_state(self):
        pass