from gi_loadouts.type.char import BaseStat, Char
from gi_loadouts.type.rare import Rare
from gi_loadouts.type.stat import STAT
from gi_loadouts.type.vson import Vision
from gi_loadouts.type.weap import WeaponType


class Ganyu(Char):
    __statdata__: dict = {0: 0.0, 1: 0.0, 2: 9.6, 3: 19.2, 4: 19.2, 5: 28.8, 6: 38.4}
    __statname__: STAT = STAT.critical_damage_perc
    name: str = "Ganyu"
    rare: Rare = Rare.Star_5
    base: BaseStat = BaseStat(attack=26.068, defense=49.0606, health_points=762.656)
    ascn: BaseStat = BaseStat(attack=107.04148, defense=201.474, health_points=3131.878)
    weapon: WeaponType = WeaponType.bow
    vision: Vision = Vision.cryo
    cons_name: str = "Sinae Unicornis"
    afln: str = "Yuehai Pavilion"
    head: str = "Plenilune Gaze"