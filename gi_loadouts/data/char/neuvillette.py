from gi_loadouts.type.char import BaseStat, Char
from gi_loadouts.type.rare import Rare
from gi_loadouts.type.stat import STAT
from gi_loadouts.type.vson import Vision
from gi_loadouts.type.weap import WeaponType


class Neuvillette(Char):
    __statdata__: dict = {0: 0.0, 1: 0.0, 2: 9.6, 3: 19.2, 4: 19.2, 5: 28.8, 6: 38.4}
    __statname__: STAT = STAT.critical_damage_perc
    name: str = "Neuvillette"
    rare: Rare = Rare.Star_5
    base: BaseStat = BaseStat(attack=16.218, defense=44.8725, health_points=1143.984)
    ascn: BaseStat = BaseStat(attack=66.595, defense=184.275, health_points=4697.8169)
    weapon: WeaponType = WeaponType.catalyst
    vision: Vision = Vision.hydro
    cons_name: str = "Leviathan Judicator"
    afln: str = "Court of Fontaine"
    head: str = "Ordainer of Inexorable Judgment"