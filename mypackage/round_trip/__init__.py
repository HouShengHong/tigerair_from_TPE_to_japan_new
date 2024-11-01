from ..flight import flight as _flight
import datetime as _datetime

class round_trip:
    def __init__(
        self,
        outbound:_flight = None,
        inbound:_flight = None,
    ):
        self.outbound = outbound if outbound is not None else _flight()
        self.inbound = inbound if inbound is not None else _flight()

    def discountedTotalAmount():
        pass

    def __str__(self):
        return f'''{'\033[96m'}{'outbound':>69}{'\033[0m'}|{'\033[94m'}{'inbound':<69}{'\033[0m'}
{self.outbound.legSellKey:>56} : {'legSellKey':^21} : {self.inbound.legSellKey:<56}
{self.outbound.origin:>56} : {'origin':^21} : {self.inbound.origin:<56}
{self.outbound.destination:>56} : {'destination':^21} : {self.inbound.destination:<56}
{self.outbound.departureTime.strftime("%Y-%m-%d %H:%M:%S"):>56} : {'departureTime':^21} : {self.inbound.departureTime.strftime("%Y-%m-%d %H:%M:%S"):<56}
{self.outbound.arrivalTime.strftime("%Y-%m-%d %H:%M:%S"):>56} : {'arrivalTime':^21} : {self.inbound.arrivalTime.strftime("%Y-%m-%d %H:%M:%S"):<56}
{self.outbound.remainingSeat:>56} : {'remainingSeat':^21} : {self.inbound.remainingSeat:<56}
{self.outbound.availableCount:>56} : {'availableCount':^21} : {self.inbound.availableCount:<56}
{self.outbound.totalAmount:>56} : {'totalAmount':^21} : {self.inbound.totalAmount:<56}
{self.outbound.discountedTotalAmount:>56} : {'discountedTotalAmount':^21} : {self.inbound.discountedTotalAmount:<56}'''
    







