from gi_loadouts.type.char import BaseStat, Char
from gi_loadouts.type.rare import Rare
from gi_loadouts.type.stat import STAT
from gi_loadouts.type.vson import Vision
from gi_loadouts.type.weap import WeaponType


class Xinyan(Char):
    __statdata__: dict = {0: 0.0, 1: 0.0, 2: 6.0, 3: 12.0, 4: 12.0, 5: 18.0, 6: 24.0}
    __statname__: STAT = STAT.attack_perc
    name: str = "Xinyan"
    rare: Rare = Rare.Star_4
    base: BaseStat = BaseStat(attack=20.83536, defense=66.95325, health_points=939.1447)
    ascn: BaseStat = BaseStat(attack=74.55029, defense=239.5575, health_points=3360.243)
    weapon: WeaponType = WeaponType.claymore
    vision: Vision = Vision.pyro
    cons_name: str = "Fila Ignium"
    afln: str = "\"The Red Strings\""
    head: str = "Blazing Riff"