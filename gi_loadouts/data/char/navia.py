from gi_loadouts.type.char import BaseStat, Char
from gi_loadouts.type.rare import Rare
from gi_loadouts.type.stat import STAT
from gi_loadouts.type.vson import Vision
from gi_loadouts.type.weap import WeaponType


class Navia(Char):
    __statdata__: dict = {0: 0.0, 1: 0.0, 2: 9.6, 3: 19.2, 4: 19.2, 5: 28.8, 6: 38.4}
    __statname__: STAT = STAT.critical_damage_perc
    name: str = "Navia"
    rare: Rare = Rare.Star_5
    base: BaseStat = BaseStat(attack=27.3714, defense=61.74456, health_points=984.78)
    ascn: BaseStat = BaseStat(attack=112.3935546875, defense=253.56239318848, health_points=4044.0373535156)
    weapon: WeaponType = WeaponType.claymore
    vision: Vision = Vision.geo
    cons_name: str = "Rosa Multiflora"
    afln: str = "Spina di Rosula"
    head: str = "Helm of the Radiant Rose"