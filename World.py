import tiles.Tile
import game_graphics.Sprite


class World:

    map_width = 20
    map_height = 20
    tiles_hash = []

    camera_x = 0
    camera_y = 0

    def __init__(self):
        self.objects = []
        World.tiles_hash = [[x for x in range(World.map_width)] for y in range(World.map_height)]
        for y in range(World.map_height):
            for x in range(World.map_width):
                World.tiles_hash[y][x] = tiles.Tile.Tile(game_graphics.Sprite.grass_sprite)

        World.tiles_hash[10][10] = tiles.Tile.Tile(game_graphics.Sprite.stone_sprite, solid=True)

    def update(self):
        for obj in self.objects:
            obj.update()

    def render(self, display):
        for y in range((World.camera_y >> 5), (World.camera_y >> 5) + (display.height >> 5) + 2):
            for x in range((World.camera_x >> 5), (World.camera_x >> 5) + (display.width >> 5) + 2):
                if y < World.map_height and y >= 0 and x < World.map_width and x >= 0:
                    display.canvas.blit(World.tiles_hash[y][x].sprite.pic, ((x << 5) - World.camera_x, (y << 5) - World.camera_y))


        for obj in self.objects:
            obj.render(display)


