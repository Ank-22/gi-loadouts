from gi_loadouts.type.char import BaseStat, Char
from gi_loadouts.type.rare import Rare
from gi_loadouts.type.stat import STAT
from gi_loadouts.type.vson import Vision
from gi_loadouts.type.weap import WeaponType


class ShikanoinHeizou(Char):
    __statdata__: dict = {0: 0.0, 1: 0.0, 2: 6.0, 3: 12.0, 4: 12.0, 5: 18.0, 6: 24.0}
    __statname__: STAT = STAT.damage_bonus_anemo_perc
    name: str = "Shikanoin Heizou"
    rare: Rare = Rare.Star_4
    base: BaseStat = BaseStat(attack=18.87648, defense=57.33945, health_points=893.5552)
    ascn: BaseStat = BaseStat(attack=67.54129, defense=205.1595, health_points=3197.1245)
    weapon: WeaponType = WeaponType.catalyst
    vision: Vision = Vision.anemo
    cons_name: str = "Cervus Minor"
    afln: str = "Tenryou Commission"
    head: str = "Analytical Harmony"