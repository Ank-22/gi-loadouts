from enum import Enum

from pydantic import BaseModel

from gi_loadouts.type.char.cons import Cons
from gi_loadouts.type.char.mult import Mult, Secs
from gi_loadouts.type.levl import Level
from gi_loadouts.type.rare import Rare
from gi_loadouts.type.stat import STAT
from gi_loadouts.type.vson import Vision
from gi_loadouts.type.weap import WeaponType


class CharName(str, Enum):
    """
    Set of characters possible
    """
    aether = "Aether"
    albedo = "Albedo"
    alhaitham = "Alhaitham"
    aloy = "Aloy"
    amber = "Amber"
    arataki_itto = "Arataki Itto"
    arlecchino = "Arlecchino"
    baizhu = "Baizhu"
    barbara = "Barbara"
    beidou = "Beidou"
    bennett = "Bennett"
    candace = "Candace"
    charlotte = "Charlotte"
    chevreuse = "Chevreuse"
    chiori = "Chiori"
    chongyun = "Chongyun"
    clorinde = "Clorinde"
    collei = "Collei"
    cyno = "Cyno"
    dehya = "Dehya"
    diluc = "Diluc"
    diona = "Diona"
    dori = "Dori"
    emilie = "Emilie"
    eula = "Eula"
    faruzan = "Faruzan"
    fischl = "Fischl"
    freminet = "Freminet"
    furina = "Furina"
    gaming = "Gaming"
    ganyu = "Ganyu"
    gorou = "Gorou"
    hu_tao = "Hu Tao"
    jean = "Jean"
    kaedehara_kazuha = "Kaedehara Kazuha"
    kamisato_ayaka = "Kamisato Ayaka"
    kamisato_ayato = "Kamisato Ayato"
    kaeya = "Kaeya"
    kaveh = "Kaveh"
    keqing = "Keqing"
    kirara = "Kirara"
    klee = "Klee"
    kujou_sara = "Kujou Sara"
    kuki_shinobu = "Kuki Shinobu"
    layla = "Layla"
    lisa = "Lisa"
    lumine = "Lumine"
    lynette = "Lynette"
    lyney = "Lyney"
    mika = "Mika"
    mona = "Mona"
    nahida = "Nahida"
    navia = "Navia"
    neuvillette = "Neuvillette"
    nilou = "Nilou"
    ningguang = "Ningguang"
    noelle = "Noelle"
    qiqi = "Qiqi"
    raiden_shogun = "Raiden Shogun"
    razor = "Razor"
    rosaria = "Rosaria"
    sangonomiya_kokomi = "Sangonomiya Kokomi"
    sayu = "Sayu"
    sethos = "Sethos"
    shenhe = "Shenhe"
    shikanoin_heizou = "Shikanoin Heizou"
    sigewinne = "Sigewinne"
    sucrose = "Sucrose"
    tartaglia = "Tartaglia"
    thoma = "Thoma"
    tighnari = "Tighnari"
    venti = "Venti"
    wanderer = "Wanderer"
    wriothesley = "Wriothesley"
    xiangling = "Xiangling"
    xianyun = "Xianyun"
    xiao = "Xiao"
    xingqiu = "Xingqiu"
    xinyan = "Xinyan"
    yae_miko = "Yae Miko"
    yanfei = "Yanfei"
    yaoyao  = "Yaoyao"
    yelan = "Yelan"
    yoimiya = "Yoimiya"
    yun_jin = "Yun Jin"
    zhongli = "Zhongli"


class SecoStat(BaseModel):
    """
    Data class for secondary stat of a character
    """
    stat_name: STAT = STAT.none
    stat_data: float = 0.0


class Char(BaseModel):
    """
    Character primitive
    """
    __statname__: STAT = STAT.none
    __statdata__: dict = {}
    rare: Rare = Rare.Star_4
    name: CharName = CharName.lumine
    levl: Level = Level.Level_01_20_Rank_0
    cons: Cons = Cons.Constellation_1
    vision: Vision = Vision.none
    weapon: WeaponType = WeaponType.none
    cons_name: str = ""
    afln: str = ""
    head: str = ""

    @property
    def attack(self) -> float:
        """
        Calculate the statistics associated with the attack potential of a character based on their level, rank and ascension value

        :return: Attack potential associated with the character
        """
        return self.base.attack * Mult[self.levl.value.qant][self.rare] + Secs[self.levl.value.rank] * self.ascn.attack

    @property
    def defense(self) -> float:
        """
        Calculate the statistics associated with the defense potential of a character based on their level, rank and ascension value

        :return: Defense potential associated with the character
        """
        return self.base.defense * Mult[self.levl.value.qant][self.rare] + Secs[self.levl.value.rank] * self.ascn.defense

    @property
    def health_points(self) -> float:
        """
        Calculate the statistics associated with the health points potential of a character based on their level, rank and ascension value

        :return: Health points potential associated with the character
        """
        return self.base.health_points * Mult[self.levl.value.qant][self.rare] + Secs[self.levl.value.rank] * self.ascn.health_points

    @property
    def seco(self) -> SecoStat:
        """
        Calculate the statistics associated with the health points potential of a character based on their rank

        :return: Secondary statistics associated with the character
        """
        return SecoStat(stat_name=self.__statname__, stat_data=self.__statdata__[self.levl.value.rank.value])


class BaseStat(BaseModel):
    """
    Base stats of a character

    SUSPECTED TO BE RESIDUAL CODE
    """
    attack: float = 0.0
    defense: float = 0.0
    health_points: float = 0.0