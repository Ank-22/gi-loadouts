from gi_loadouts.type.char import BaseStat, Char
from gi_loadouts.type.rare import Rare
from gi_loadouts.type.stat import STAT
from gi_loadouts.type.vson import Vision
from gi_loadouts.type.weap import WeaponType


class Candace(Char):
    __statdata__: dict = {0: 0.0, 1: 0.0, 2: 6.0, 3: 12.0, 4: 12.0, 5: 18.0, 6: 24.0}
    __statname__: STAT = STAT.health_points_perc
    name: str = "Candace"
    rare: Rare = Rare.Star_4
    base: BaseStat = BaseStat(attack=17.808, defense=57.225, health_points=911.791)
    ascn: BaseStat = BaseStat(attack=63.7182, defense=204.75, health_points=3262.3718)
    weapon: WeaponType = WeaponType.polearm
    vision: Vision = Vision.hydro
    cons_name: str = "Sagitta Scutum"
    afln: str = "Aaru Village"
    head: str = "Golden Vow"