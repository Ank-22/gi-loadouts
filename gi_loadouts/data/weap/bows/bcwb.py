from typing import List

from gi_loadouts.type.rare import Rare
from gi_loadouts.type.weap import Bow, WeaponStat, WeaponStatType
from gi_loadouts.type.weap.base.tier import Tier


class BlackcliffWarbow(Bow):
    name: str = "Blackcliff Warbow"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.critical_damage_perc, stat_data=8.0)
    tier: Tier = Tier.Tier_3
    rare: Rare = Rare.Star_4
    refi_name: str = "Press the Advantage"
    refi_list: List[str] = [
        "After defeating an opponent, ATK is increased by 12% for 30s. This effect has a maximum of 3 stacks, and the duration of each stack is independent of the others.",
        "After defeating an opponent, ATK is increased by 15% for 30s. This effect has a maximum of 3 stacks, and the duration of each stack is independent of the others.",
        "After defeating an opponent, ATK is increased by 18% for 30s. This effect has a maximum of 3 stacks, and the duration of each stack is independent of the others.",
        "After defeating an opponent, ATK is increased by 21% for 30s. This effect has a maximum of 3 stacks, and the duration of each stack is independent of the others.",
        "After defeating an opponent, ATK is increased by 24% for 30s. This effect has a maximum of 3 stacks, and the duration of each stack is independent of the others.",
    ]
    file: str = "bcwb"