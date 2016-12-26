import tiles.Tile
import game_graphics.Sprite
import pygame


class World:

    map_width = 60
    map_height = 80
    tiles_hash = []
    mobs = []
    projectiles = []

    camera_x = 0
    camera_y = 0

    def __init__(self):

        map_pixels = pygame.surfarray.array2d(game_graphics.Sprite.map.pic)
        World.tiles_hash = [[x for x in range(World.map_width)] for y in range(World.map_height)]

        for y in range(World.map_height):
            for x in range(World.map_width):
                set_tile(map_pixels[x][y], x, y)

        World.tiles_hash[10][10] = tiles.Tile.Tile(game_graphics.Sprite.grass, solid=True)

    def update(self):

        for mob in World.mobs:
            mob.update()

        for mob in World.mobs:
            mob.update_tile()

        for projectile in World.projectiles:
            projectile.update()

        for projectile in World.projectiles:
            projectile.update_tile()

        for mob in World.mobs:
            if mob.removed:
                if mob.last_tile != None and mob in mob.last_tile.mobs:
                    mob.last_tile.mobs.remove(mob)
                if mob.current_tile != None and mob in mob.current_tile.mobs:
                    mob.current_tile.mobs.remove(mob)
                World.mobs.remove(mob)

        for projectile in World.projectiles:
            if projectile.removed:
                if projectile.last_tile != None and projectile in projectile.last_tile.projectiles:
                    projectile.last_tile.projectiles.remove(projectile)
                if projectile.current_tile != None and projectile in projectile.current_tile.projectiles:
                    projectile.current_tile.projectiles.remove(projectile)
                World.projectiles.remove(projectile)


    def render(self, display):
        for y in range((World.camera_y >> 5), (World.camera_y >> 5) + (display.height >> 5) + 2):
            for x in range((World.camera_x >> 5), (World.camera_x >> 5) + (display.width >> 5) + 2):
                if y < World.map_height and y >= 0 and x < World.map_width and x >= 0:
                    display.canvas.blit(World.tiles_hash[y][x].sprite.pic, ((x << 5) - World.camera_x, (y << 5) - World.camera_y))


        for y in range((World.camera_y >> 5), (World.camera_y >> 5) + (display.height >> 5) + 2):
            for x in range((World.camera_x >> 5), (World.camera_x >> 5) + (display.width >> 5) + 2):
                if y < World.map_height and y >= 0 and x < World.map_width and x >= 0:
                    for mob in World.tiles_hash[y][x].mobs:
                        mob.render(display)


        for y in range((World.camera_y >> 5), (World.camera_y >> 5) + (display.height >> 5) + 2):
            for x in range((World.camera_x >> 5), (World.camera_x >> 5) + (display.width >> 5) + 2):
                if y < World.map_height and y >= 0 and x < World.map_width and x >= 0:
                    for projectile in World.tiles_hash[y][x].projectiles:
                        projectile.render(display)





def set_tile(color, x, y):
    print(color)
    if color == 950016:
        World.tiles_hash[y][x] = tiles.Tile.Tile(game_graphics.Sprite.grass)
        return

    if color == 8382975:
        World.tiles_hash[y][x] = tiles.Tile.Tile(game_graphics.Sprite.sand)
        return

    if color == 16749568:
        World.tiles_hash[y][x] = tiles.Tile.Tile(game_graphics.Sprite.water, solid=True)
        return

    if color == 4151679:
        World.tiles_hash[y][x] = tiles.Tile.Tile(game_graphics.Sprite.dirt)
        return

    if color == 8421504:
        World.tiles_hash[y][x] = tiles.Tile.Tile(game_graphics.Sprite.stone, solid=True, high=True)
        return

    if color == 10526880:
        World.tiles_hash[y][x] = tiles.Tile.Tile(game_graphics.Sprite.stone_source, solid=True, high=True)
        return

    if color == 27391:
        World.tiles_hash[y][x] = tiles.Tile.Tile(game_graphics.Sprite.wooden_wall, solid=True, high=True)
        return

    World.tiles_hash[y][x] = tiles.Tile.Tile(game_graphics.Sprite.grass)