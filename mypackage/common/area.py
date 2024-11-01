from enum import Enum as _Enum
from airport import Airport as _Airport

class Area(_Enum):

    kanto              = (_Airport.NRT.value,_Airport.HND.value,_Airport.IBR.value,)

    kansai_and_shikoku = (_Airport.KIX.value,_Airport.OKJ.value,_Airport.KCZ.value,)

    kyushu             = (_Airport.FUK.value,_Airport.HSG.value,_Airport.OKA.value,)

    chubu              = (_Airport.NGO.value,_Airport.KMQ.value,_Airport.KIJ.value,)

    tohoku             = (_Airport.SDJ.value,_Airport.AXT.value,_Airport.HNA.value,_Airport.FKS.value,)

    hokkaido           = (_Airport.HKD.value,_Airport.CTS.value,_Airport.AKJ.value,)


print(Area.hokkaido.value) 
print(_Airport.hokkaido.value)
print(Area.hokkaido.value == _Airport.hokkaido.value)