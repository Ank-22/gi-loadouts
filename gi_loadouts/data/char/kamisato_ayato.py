from gi_loadouts.type.char import BaseStat, Char
from gi_loadouts.type.rare import Rare
from gi_loadouts.type.stat import STAT
from gi_loadouts.type.vson import Vision
from gi_loadouts.type.weap import WeaponType


class KamisatoAyato(Char):
    __statdata__: dict = {0: 0.0, 1: 0.0, 2: 9.6, 3: 19.2, 4: 19.2, 5: 28.8, 6: 38.4}
    __statname__: STAT = STAT.critical_damage_perc
    name: str = "Kamisato Ayato"
    rare: Rare = Rare.Star_5
    base: BaseStat = BaseStat(attack=23.275, defense=59.83, health_points=1067.7184)
    ascn: BaseStat = BaseStat(attack=95.57275, defense=245.7, health_points=4384.629)
    weapon: WeaponType = WeaponType.sword
    vision: Vision = Vision.hydro
    cons_name: str = "Cypressus Custos"
    afln: str = "Yashiro Commission"
    head: str = "Pillar of Fortitude"