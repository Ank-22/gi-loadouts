from gi_loadouts.type.char import BaseStat, Char
from gi_loadouts.type.rare import Rare
from gi_loadouts.type.stat import STAT
from gi_loadouts.type.vson import Vision
from gi_loadouts.type.weap import WeaponType


class KamisatoAyaka(Char):
    __statdata__: dict = {0: 0.0, 1: 0.0, 2: 9.6, 3: 19.2, 4: 19.2, 5: 28.8, 6: 38.4}
    __statname__: STAT = STAT.critical_damage_perc
    name: str = "Kamisato Ayaka"
    rare: Rare = Rare.Star_5
    base: BaseStat = BaseStat(attack=26.6266, defense=61.0266, health_points=1000.986)
    ascn: BaseStat = BaseStat(attack=109.33523, defense=250.614, health_points=4110.59)
    weapon: WeaponType = WeaponType.sword
    vision: Vision = Vision.cryo
    cons_name: str = "Grus Nivis"
    afln: str = "Yashiro Commission"
    head: str = "Frostflake Heron"