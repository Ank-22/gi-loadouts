from gi_loadouts.type.char import BaseStat, Char
from gi_loadouts.type.rare import Rare
from gi_loadouts.type.stat import STAT
from gi_loadouts.type.vson import Vision
from gi_loadouts.type.weap import WeaponType


class Lisa(Char):
    __statdata__: dict = {0: 0.0, 1: 0.0, 2: 24.0, 3: 48.0, 4: 48.0, 5: 72.0, 6: 96.0}
    __statname__: STAT = STAT.elemental_mastery
    name: str = "Lisa"
    rare: Rare = Rare.Star_4
    base: BaseStat = BaseStat(attack=19.41072, defense=48.069, health_points=802.3761)
    ascn: BaseStat = BaseStat(attack=69.452835, defense=171.99, health_points=2870.8872)
    weapon: WeaponType = WeaponType.catalyst
    vision: Vision = Vision.electro
    cons_name: str = "Tempus Fugit"
    afln: str = "Knights of Favonius"
    head: str = "Witch of Purple Rose"