from gi_loadouts.type.char import BaseStat, Char
from gi_loadouts.type.rare import Rare
from gi_loadouts.type.stat import STAT
from gi_loadouts.type.vson import Vision
from gi_loadouts.type.weap import WeaponType


class Zhongli(Char):
    __statdata__: dict = {0: 0.0, 1: 0.0, 2: 7.2, 3: 14.4, 4: 14.4, 5: 21.6, 6: 28.8}
    __statname__: STAT = STAT.damage_bonus_geo_perc
    name: str = "Zhongli"
    rare: Rare = Rare.Star_5
    base: BaseStat = BaseStat(attack=19.551, defense=57.4368, health_points=1143.984)
    ascn: BaseStat = BaseStat(attack=80.2811, defense=235.872, health_points=4697.817)
    weapon: WeaponType = WeaponType.polearm
    vision: Vision = Vision.geo
    cons_name: str = "Lapis Dei"
    afln: str = "Liyue Harbor"
    head: str = "Vago Mundo"