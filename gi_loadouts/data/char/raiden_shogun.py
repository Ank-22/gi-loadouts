from gi_loadouts.type.char import BaseStat, Char
from gi_loadouts.type.rare import Rare
from gi_loadouts.type.stat import STAT
from gi_loadouts.type.vson import Vision
from gi_loadouts.type.weap import WeaponType


class RaidenShogun(Char):
    __statdata__: dict = {0: 0.0, 1: 0.0, 2: 8.0, 3: 16.0, 4: 16.0, 5: 24.0, 6: 32.0}
    __statname__: STAT = STAT.energy_recharge_perc
    name: str = "Raiden Shogun"
    rare: Rare = Rare.Star_5
    base: BaseStat = BaseStat(attack=26.2542, defense=61.44541, health_points=1004.79926)
    ascn: BaseStat = BaseStat(attack=107.80606, defense=252.3339, health_points=4126.249)
    weapon: WeaponType = WeaponType.polearm
    vision: Vision = Vision.electro
    cons_name: str = "Imperatrix Umbrosa"
    afln: str = "Inazuma City"
    head: str = "Plane of Euthymia"