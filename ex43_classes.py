# * Map
#   - next_scene
#   - opening_scene
# * Engine
#   - play
# * Scene
#   - enter
#   * Death
#   * Central Corridor
#   * Laser Weapon Armory
#   * The Brigde
#   * Escape Pod

class Scene(object):
    def enter(self):
        pass

class Engine(object):
    def __init__(self, scene_map):
        pass
    def play(self):
        pass

class Death(Scene):
    def enter(self):
        pass
class CentralCorridor(Scene):
    def enter(self):
        pass
class LaseWeaponArmery(Scene):
    def enter(self):
        pass
class TheBrigde(Scene):
    def enter(self):
        pass
class EscapePod(Scene):
    def enter(self):
        pass

class Map(object):
    def __init__(self, start_scene):
        pass
    def next_scene(self, scene_name):
        pass
    def opening_scene(self):
        pass

a_map = Map("central_corridor")
a_game = Engine(a_map)
a_game.play()