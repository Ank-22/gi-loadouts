from gi_loadouts.type.char import BaseStat, Char
from gi_loadouts.type.rare import Rare
from gi_loadouts.type.stat import STAT
from gi_loadouts.type.vson import Vision
from gi_loadouts.type.weap import WeaponType


class SangonomiyaKokomi(Char):
    __statdata__: dict = {0: 0.0, 1: 0.0, 2: 7.2, 3: 14.4, 4: 14.4, 5: 21.6, 6: 28.8}
    __statname__: STAT = STAT.damage_bonus_hydro_perc
    name: str = "Sangonomiya Kokomi"
    rare: Rare = Rare.Star_5
    base: BaseStat = BaseStat(attack=18.2476, defense=51.15465, health_points=1048.652)
    ascn: BaseStat = BaseStat(attack=74.92904, defense=210.0735, health_points=4306.332)
    weapon: WeaponType = WeaponType.catalyst
    vision: Vision = Vision.hydro
    cons_name: str = "Dracaena Somnolenta"
    afln: str = "Watatsumi Island"
    head: str = "Pearl of Wisdom"