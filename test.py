from mypackage.flight import flight

from mypackage.round_trip import round_trip

import datetime

import warnings

a = flight(
    legSellKey            = 'IT~ 216~ ~~TPE~07/07/2024 00:10~HND~07/07/2024 04:25~~',
    origin                = 'TPE',
    destination           = 'HND',
    departureTime         = datetime.datetime.strptime('2024-07-07 00:10:00', "%Y-%m-%d %H:%M:%S") ,
    arrivalTime           = datetime.datetime.strptime('2024-07-07 04:25:00', "%Y-%m-%d %H:%M:%S"),
    remainingSeat         = 4,
    availableCount        = 4,
    totalAmount           = 7799,
    discountedTotalAmount = 7799,
)

b = flight(
    legSellKey            = 'IT~ 217~ ~~HND~07/07/2024 05:25~TPE~07/07/2024 08:00~~',
    origin                = 'HND',
    destination           = 'TPE',
    departureTime         = datetime.datetime.strptime('2024-07-07 05:25:00', "%Y-%m-%d %H:%M:%S") ,
    arrivalTime           = datetime.datetime.strptime('2024-07-07 08:00:00', "%Y-%m-%d %H:%M:%S"),
    remainingSeat         = 7,
    availableCount        = 5,
    totalAmount           = 5699,
    discountedTotalAmount = 5699,
)

a_b = round_trip(a,b)
print(a_b)

warnings.warn('abc')