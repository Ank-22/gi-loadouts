from gi_loadouts.type.char import BaseStat, Char
from gi_loadouts.type.rare import Rare
from gi_loadouts.type.stat import STAT
from gi_loadouts.type.vson import Vision
from gi_loadouts.type.weap import WeaponType


class AratakiItto(Char):
    __statdata__: dict = {0: 0.0, 1: 0.0, 2: 4.8, 3: 9.6, 4: 9.6, 5: 14.4, 6: 19.2}
    __statname__: STAT = STAT.critical_rate_perc
    name: str = "Arataki Itto"
    rare: Rare = Rare.Star_5
    base: BaseStat = BaseStat(attack=17.689, defense=74.66784, health_points=1000.986)
    ascn: BaseStat = BaseStat(attack=72.63529, defense=306.6336, health_points=4110.59)
    weapon: WeaponType = WeaponType.claymore
    vision: Vision = Vision.geo
    cons_name: str = "Taurus Iracundus"
    afln: str = "Arataki Gang"
    head: str = "Hanamizaka Heroics"