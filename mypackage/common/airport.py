from enum import (Enum as _Enum ,
    auto as _auto)


class Airport(_Enum):
    @staticmethod
    def _generate_next_value_(name, start, count, last_values):
        return name

    TPE = _auto()

    NRT = _auto()
    HND = _auto()
    IBR = _auto()
    kanto = (NRT,HND,IBR,)

    KIX = _auto()
    OKJ = _auto()
    KCZ = _auto()
    kansai_and_shikoku = (KIX,OKJ,KCZ,)

    FUK = _auto()
    HSG = _auto()
    OKA = _auto()
    kyushu = (FUK,HSG,OKA,)
    
    NGO = _auto()
    KMQ = _auto()
    KIJ = _auto()
    chubu = (NGO,KMQ,KIJ,)

    SDJ = _auto()
    AXT = _auto()
    HNA = _auto()
    FKS = _auto()
    tohoku = (SDJ,AXT,HNA,FKS,)

    HKD = _auto()
    CTS = _auto()
    AKJ = _auto()
    hokkaido = (HKD,CTS,AKJ,)






