from gi_loadouts.type.char import BaseStat, Char
from gi_loadouts.type.rare import Rare
from gi_loadouts.type.stat import STAT
from gi_loadouts.type.vson import Vision
from gi_loadouts.type.weap import WeaponType


class Mona(Char):
    __statdata__: dict = {0: 0.0, 1: 0.0, 2: 8.0, 3: 16.0, 4: 16.0, 5: 24.0, 6: 32.0}
    __statname__: STAT = STAT.energy_recharge_perc
    name: str = "Mona"
    rare: Rare = Rare.Star_5
    base: BaseStat = BaseStat(attack=22.344, defense=50.8555, health_points=810.322)
    ascn: BaseStat = BaseStat(attack=91.74984, defense=208.845, health_points=3327.62)
    weapon: WeaponType = WeaponType.catalyst
    vision: Vision = Vision.hydro
    cons_name: str = "Astrolabos"
    afln: str = "Mondstadt"
    head: str = "Astral Reflection"