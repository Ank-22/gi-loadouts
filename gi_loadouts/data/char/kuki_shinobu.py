from gi_loadouts.type.char import BaseStat, Char
from gi_loadouts.type.rare import Rare
from gi_loadouts.type.stat import STAT
from gi_loadouts.type.vson import Vision
from gi_loadouts.type.weap import WeaponType


class KukiShinobu(Char):
    __statdata__: dict = {0: 0.0, 1: 0.0, 2: 6.0, 3: 12.0, 4: 12.0, 5: 18.0, 6: 24.0}
    __statname__: STAT = STAT.health_points_perc
    name: str = "Kuki Shinobu"
    rare: Rare = Rare.Star_4
    base: BaseStat = BaseStat(attack=17.808, defense=62.9475, health_points=1030.3239)
    ascn: BaseStat = BaseStat(attack=63.7182, defense=225.225, health_points=3686.4802)
    weapon: WeaponType = WeaponType.sword
    vision: Vision = Vision.electro
    cons_name: str = "Tribulatio Demptio"
    afln: str = "Arataki Gang"
    head: str = "Mender of Tribulations"