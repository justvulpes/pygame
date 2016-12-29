"""MenuWorld."""

import tiles.Tile
import game_graphics.Sprite
import pygame
import objects.building.Wall
import objects.mobs.Player


class MenuWorld:
    """MenuWorld."""

    map_width = 60
    map_height = 80
    tiles_hash = []
    mobs = []

    camera_x = 0
    camera_y = 0

    def __init__(self):
        """Constructor."""


        map_pixels = pygame.surfarray.array2d(game_graphics.Sprite.map.pic)
        MenuWorld.tiles_hash = [[x for x in range(MenuWorld.map_width)] for y in range(MenuWorld.map_height)]

        for y in range(MenuWorld.map_height):
            for x in range(MenuWorld.map_width):
                set_tile(map_pixels[x][y], x, y)

        MenuWorld.tiles_hash[10][10] = tiles.Tile.Tile(game_graphics.Sprite.grass, solid=True)



    @staticmethod
    def update():
        """Update."""

        for mob in MenuWorld.mobs:
            mob.update()

        for mob in MenuWorld.mobs:
            mob.update_tile()

        for mob in MenuWorld.mobs:
            if mob.removed:
                if mob.last_tile is not None and mob in mob.last_tile.mobs:
                    mob.last_tile.mobs.remove(mob)
                if mob.current_tile is not None and mob in mob.current_tile.mobs:
                    mob.current_tile.mobs.remove(mob)
                MenuWorld.mobs.remove(mob)


    @staticmethod
    def render(display):
        """Render."""
        for y in range((MenuWorld.camera_y >> 5), (MenuWorld.camera_y >> 5) + (display.height >> 5) + 2):
            for x in range((MenuWorld.camera_x >> 5), (MenuWorld.camera_x >> 5) + (display.width >> 5) + 2):
                if MenuWorld.map_height > y >= 0 and MenuWorld.map_width > x >= 0:
                    display.canvas.blit(MenuWorld.tiles_hash[y][x].sprite.pic, ((x << 5) - MenuWorld.camera_x, (y << 5) - MenuWorld.camera_y))

        for y in range((MenuWorld.camera_y >> 5), (MenuWorld.camera_y >> 5) + (display.height >> 5) + 2):
            for x in range((MenuWorld.camera_x >> 5), (MenuWorld.camera_x >> 5) + (display.width >> 5) + 2):
                if MenuWorld.map_height > y >= 0 and MenuWorld.map_width > x >= 0:
                    if MenuWorld.tiles_hash[y][x].mask is not None:
                        display.canvas.blit(MenuWorld.tiles_hash[y][x].mask.pic, ((x << 5) - MenuWorld.camera_x, (y << 5) - MenuWorld.camera_y))


def set_tile(color, x, y):
    """Set tile."""
    if color == 950016:
        MenuWorld.tiles_hash[y][x] = tiles.Tile.Tile(game_graphics.Sprite.grass)
        return

    if color == 8382975:
        MenuWorld.tiles_hash[y][x] = tiles.Tile.Tile(game_graphics.Sprite.sand)
        return

    if color == 16749568:
        MenuWorld.tiles_hash[y][x] = tiles.Tile.Tile(game_graphics.Sprite.water, solid=True)
        return

    if color == 4151679:
        MenuWorld.tiles_hash[y][x] = tiles.Tile.Tile(game_graphics.Sprite.dirt)
        return

    if color == 8421504:
        MenuWorld.tiles_hash[y][x] = tiles.Tile.Tile(game_graphics.Sprite.stone, solid=True, high=True)
        return

    if color == 10526880:
        MenuWorld.tiles_hash[y][x] = tiles.Tile.Tile(game_graphics.Sprite.stone_source, solid=True, high=True)
        return

    if color == 27391:
        MenuWorld.tiles_hash[y][x] = tiles.Tile.Tile(game_graphics.Sprite.dirt, solid=False, high=False)
        MenuWorld.tiles_hash[y][x].building = objects.building.Wall.Wall(x,y)
        return

    if color == 255:
        MenuWorld.tiles_hash[y][x] = tiles.Tile.Tile(game_graphics.Sprite.grass, solid=True, high=True, mask=game_graphics.Sprite.christmas_tree_lower)
        return

    if color == 127:
        MenuWorld.tiles_hash[y][x] = tiles.Tile.Tile(game_graphics.Sprite.grass, solid=False, high=False, mask=game_graphics.Sprite.christmas_tree_upper)
        return

    if color == 15564799:
        MenuWorld.tiles_hash[y][x] = tiles.Tile.Tile(game_graphics.Sprite.snow, solid=True, high=True, mask=game_graphics.Sprite.christmas_tree_lower)
        return

    if color == 14418175:
        MenuWorld.tiles_hash[y][x] = tiles.Tile.Tile(game_graphics.Sprite.snow, solid=False, high=False, mask=game_graphics.Sprite.christmas_tree_upper)
        return

    if color == 16777215:
        MenuWorld.tiles_hash[y][x] = tiles.Tile.Tile(game_graphics.Sprite.snow, slow=True)
        return

    MenuWorld.tiles_hash[y][x] = tiles.Tile.Tile(game_graphics.Sprite.grass)
