from typing import List

from gi_loadouts.type.rare import Rare
from gi_loadouts.type.weap import Polearm, WeaponStat, WeaponStatType
from gi_loadouts.type.weap.base.tier import Tier


class IronPoint(Polearm):
    name: str = "Iron Point"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.none, stat_data=0.0)
    tier: Tier = Tier.Tier_2
    rare: Rare = Rare.Star_2
    refi_list: List[str] = []
    file: str = "inpt"