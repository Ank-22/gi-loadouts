from gi_loadouts.type.char import BaseStat, Char
from gi_loadouts.type.rare import Rare
from gi_loadouts.type.stat import STAT
from gi_loadouts.type.vson import Vision
from gi_loadouts.type.weap import WeaponType


class HuTao(Char):
    __statdata__: dict = {0: 0.0, 1: 0.0, 2: 9.6, 3: 19.2, 4: 19.2, 5: 28.8, 6: 38.4}
    __statname__: STAT = STAT.critical_damage_perc
    name: str = "Hu Tao"
    rare: Rare = Rare.Star_5
    base: BaseStat = BaseStat(attack=8.2859, defense=68.2062, health_points=1210.7164)
    ascn: BaseStat = BaseStat(attack=34.0239, defense=280.098, health_points=4971.856)
    weapon: WeaponType = WeaponType.polearm
    vision: Vision = Vision.pyro
    cons_name: str = "Papilio Charontis"
    afln: str = "Wangsheng Funeral Parlor"
    head: str = "Fragrance in Thaw"