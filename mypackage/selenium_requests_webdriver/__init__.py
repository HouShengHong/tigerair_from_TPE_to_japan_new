__all__ = [
    'tigerair_webdriver',
]

import time as _time
import datetime as _datetime

from selenium import webdriver as _webdriver
from selenium.webdriver.common.keys import Keys as _Keys
from selenium.webdriver.common.by import By as _By
from selenium.webdriver.support.ui import WebDriverWait as _WebDriverWait
from selenium.webdriver.support import expected_conditions as _EC

import requests as _requests

from ..common.url import Url
from ..common.currency import Currency
from ..common.xpath.button import Button
from ..common.xpath.input import Input
from ..common.xpath.destination_airport import Destination_airport



from ..common.judge import (
    judge_datetime as _judge_datetime  ,
    judge_str as _judge_str
)

class tigerair_webdriver:
    """
        This class is built for graphQL's id 
    """
    def __init__ (
        self,
        destination_xpath = None,
        driver: _webdriver.Chrome = None,
        graphQL_id: str = None,
        graphQL_current_currency: str = None,
        graphQL_current_date: _datetime.date = None,
    ) -> None:

        self.destination_xpath = destination_xpath if destination_xpath is not None else Destination_airport.kanto
        self.graphQL_id = graphQL_id if graphQL_id is not None else None
        self.graphQL_current_currency = graphQL_current_currency if graphQL_current_currency is not None else Currency.TWD
        self.graphQL_current_date = graphQL_current_date if graphQL_current_date is not None else _datetime.date.today()
        match self.graphQL_current_date:
            case t if _judge_datetime.type_eq_date(t):
                match t :
                    case d if _judge_datetime.date_ge_today(d):
                        pass
                    case _ :
                        raise ValueError("'graphQL_current_date' should be greater than or equal to today. ")
            case _ :
                raise TypeError("'graphQL_current_date's type should be 'datetime.date'. ")
        self.driver = driver if driver is not None else _webdriver.Chrome()

        # if not _judge_datetime.type_eq_date(self.graphQL_current_date):
        #     raise TypeError("'graphQL_current_date's type should be 'datetime.date'. ")
        # if not _judge_datetime.date_ge_today(self.graphQL_current_date):
        #     raise ValueError("'graphQL_current_date' should be greater than or equal to today. ")

    def _driver_reopen(self):
        """
            Reopen the browser
        """
        self.driver.quit()
        self.driver = _webdriver.Chrome()

    def _driver_get(self,url = Url.index):
        """
            Loads a web page in the current browser session.

            :param url: Uses default value 'tigerair_url.index' because this help to crawl the tigerair's flights
        """
        self.driver.get(url)

    def _driver_close(self):
        """
            Closes the current window.
        """
        self.driver.close()

    def _driver_quit(self):
        """
            Closes the browser and shuts down the ChromiumDriver executable.
        """
        self.driver.quit()

    def _elem_find(self,xpath):
        """
            Find an element By xpath.

            :param xpath: element xpath
            :return: element
        """
        self.driver.find_element
        return _WebDriverWait(self.driver, 10).until(
            _EC.presence_of_element_located((_By.XPATH, xpath))
        )
    
    def _elem_click(self,xpath) -> None:
        """
            Click an element By xpath.

            :param xpath: element xpath
        """
        elem = self._elem_find(xpath)
        elem.click()
        _time.sleep(0.5)
    
    def _elem_input(self,xpath,text) -> None:
        """
            Types into element By xpath.

            :param xpath: element's xpath
        """
        elem = self._elem_find(xpath)
        elem.send_keys(text)
        elem.send_keys(_Keys.RETURN)
        _time.sleep(0.5)

    def _value_get_by_local_storage_key(self,local_storage_key:str = 'sessionId') -> str:
        """
            Gets the local storage key's value in the current window.

            :param local_storage_key: local storage key
            :default: 
                "sessionId": Includes "graphQL_id" that is necessary for crawling flights

            :return: the local storage key's value
        """
        return self.driver.execute_script(f'return window.localStorage.getItem("{local_storage_key}");')
    
    def _graphQL_id_analyze(self,value:str = None) -> str:
        """
            Analyzes 'graphQL_id' from the local storage key 'sessionId's value

            :param value: The local storage key's value. You can get the value from the method 'self._value_get_by_local_storage_key()'
            :return: graphQL id
        """
        value = value if value is not None else self._value_get_by_local_storage_key()
        return  value[value.find('|')+1:]

    def _graphQL_id_update(self) -> str:
        """
            Update self.graphQL_id By self._graphQL_id_analyze()

            :return: self.graphQL_id
        """
        self.graphQL_id = self._graphQL_id_analyze()
        return self.graphQL_id

    def graphQL_id_get(self) -> str:
        """
            Gets graphQL_id

            :return: graphQL_id
        """
        return self.graphQL_id
    
    def standard_init(self,
            destination_xpath:str = None,
        ) -> str:
        """
            Standardly initializes this class, and gets the most important value 'graphQL_id' that help to crawl the tigerair web. 

            :parma destination_xpath: Input the area's xpath where you want to go to.
                :default: tigerair_area_option_xpath.kanto
                :example: 
                    Destination_airport.kanto                           # <Recommended Usage> input the value by the class 'Destination_airport's attribute
                    '/html/body/div[6]/div/div/div/div[6]/button'       # directly input

        """
        match destination_xpath:
            case None:
                destination_xpath = self.destination_xpath
            case self.destination_xpath:
                pass
            case _ :
                self.destination_xpath = destination_xpath
        
        self._driver_get()

        self._elem_click(Button.language_bar)
        self._elem_click(Button.language_bar_option_chinese)

        self._elem_click(Button.language_bar)
        self._elem_click(Button.language_bar_option_chinese)

        self._elem_click(Button.currency_bar)
        self._elem_click(Button.currency_bar_option_TWD)

        self._elem_click(Button.round_trip)

        self._elem_click(Button.origin_airport_bar)
        self._elem_click(Button.origin_airport_bar_option_TPE)

        self._elem_click(Button.destination_airport_bar)
        self._elem_click(destination_xpath)

        self._elem_input(Input.departure_date_bar,_datetime.date.today().strftime("%Y%m%d"))
        self._elem_input(Input.return_date_bar,_datetime.date.today().strftime("%Y%m%d"))

        self._elem_click(Button.search)
        _time.sleep(5)

        return self._graphQL_id_update()

    def graphQL_currency_change(self, currency_usage:str = None):
        # default arg 
        currency_usage = currency_usage if currency_usage is not None else Currency.TWD

        # check 'currency_usage'
        if currency_usage == '' :
            raise ValueError("'currency_usage' should not be ''.")
        if not _judge_str.type_eq_str(currency_usage):
            raise TypeError("'currency_usage's type should be 'str'. ")

        response_currency_change = _requests.post(url=Url.graphQL,json=
            {
                "operationName": "appUpdateFlightSearchSession",
                "variables": {
                    "input": {
                    "id": f"{self.graphQL_id}",
                    "userCurrency": f"{currency_usage}"
                    }
                },
                "query": "mutation appUpdateFlightSearchSession($input: UpdateFlightSearchSessionInput!) {\n  appUpdateFlightSearchSession(input: $input) {\n    userCurrency\n  }\n}\n"
            }
        )
        j = response_currency_change.json()
        match j:
            case {'data': {'appUpdateFlightSearchSession': {'userCurrency': cur }}} if cur == currency_usage:
                self.graphQL_current_currency = currency_usage
                return response_currency_change
            case _ :
                raise ValueError(f"'currency_usage' is a invalid value, please check your input")

    def graphQL_date_change(self,date:_datetime.date):
        
        if not _judge_datetime.type_eq_date(date):
            raise TypeError("'Arg:date's type should be equal 'datetime.date'. ")
        if not _judge_datetime.date_ge_today(date):
            raise ValueError("'Arg:date's value should be greater than or equal to 'today'. ")

        response_date_change = _requests.post(url= Url.graphQL,json = 
            {
                "operationName": "appUpdateFlightSearchSessionSearchDate",
                "variables": {
                    "input": {
                    "id": f"{self.graphQL_id}",
                    "departureDate": f"{date.strftime('%Y-%m-%d')}",
                    "returnDate": f"{date.strftime('%Y-%m-%d')}"
                    }
                },
                "query": "fragment UpdateSearchCondition on FlightSearchSession {\n  id\n  adultCount\n  childCount\n  infantCount\n  departureDate\n  returnDate\n  promotionCode\n  stationPairs {\n    origin\n    destination\n  }\n  userCurrency\n  pricingCurrency\n  flightType\n  expiredAt\n  portal {\n    slug\n    type\n    startAt\n    endAt\n    departStartAt\n    departEndAt\n    returnStartAt\n    returnEndAt\n    flightType\n    maxPassengerCount\n    defaultPromotionCode\n    promotionCodeLength\n    isPromotionCodeDisplayed\n    voucherDetail {\n      totalLength\n      discardStartLength\n      discardEndLength\n    }\n    creditCardDetail {\n      length\n      binCode\n    }\n    portalEmbargoDates {\n      startAt\n      endAt\n    }\n  }\n}\n\nmutation appUpdateFlightSearchSessionSearchDate($input: UpdateFlightSearchSessionSearchDateInput) {\n  appUpdateFlightSearchSessionSearchDate(input: $input) {\n    ...UpdateSearchCondition\n  }\n}\n"
            }
        )
        self.graphQL_current_date = date
        return response_date_change
    
    def graphQL_search_result(self) -> _requests.models.Response:
        responese_search_result = _requests.post(url= Url.graphQL ,json={
            "operationName": "appFlightSearchResult",
            "variables": 
            {
                "id": f"{self.graphQL_id}"
            },
            "query": "query appFlightSearchResult($id: String!) {\n  appFlightSearchResult(id: $id) {\n    id\n    sessionId\n    flightType\n    journeys {\n      legs {\n        origin\n        destination\n        departureDate\n        availabilityLegs {\n          origin\n          destination\n          legSellKey\n          duration\n          overnight\n          infantSoldOut\n          infantTooMany\n          availabilitySegments {\n            origin\n            destination\n            departureTime\n            arrivalTime\n            duration\n            overnight\n            carrierCode\n            flightNumber\n            availabilitySegmentDetails {\n              equipmentType\n              totalSeat\n              soldSeat\n              remainingSeat\n              subjectToGovernmentApproval\n              availabilitySegmentDetailSsrs {\n                ssrNestCode\n                ssrLid\n                ssrSold\n                ssrValueSold\n              }\n            }\n          }\n          fares {\n            sellable\n            availableCount\n            productClass\n            carrierCode\n            ruleNumber\n            fareSellKey\n            paxFares {\n              paxType\n              ticketPrice {\n                userCurrency\n                fareAmount\n                taxAmount\n                productClassAmount\n                promotionDiscountAmount\n                discountedFareAmount\n                totalAmountWithoutTax\n                discountedTotalAmountWithoutTax\n                totalAmount\n                discountedTotalAmount\n              }\n            }\n            fareLabels {\n              translations {\n                locale\n                name\n              }\n            }\n          }\n        }\n      }\n    }\n  }\n}\n"
        })

        return responese_search_result

 # ______________________________________________________

    def destination_change_and_new_graphQL_id_update(self,destination):
        self._elem_click("/html/body/div[1]/div/div[1]/header/div[2]/div[2]/div/button[1]/span[2]/div/div")
        _time.sleep(0.5)
        self._elem_click("/html/body/div[6]/div/div[2]/div/div/div/form/div/div[2]/div/div/div/div[1]/div/div/label[2]/div/div/div/div[1]/input")
        _time.sleep(0.5)
        self._elem_click(destination)
        _time.sleep(0.5)
        self._elem_click("/html/body/div[6]/div/div[2]/div/div/div/form/div/div[3]/div[3]/button")
        _time.sleep(2)
        self._elem_click("/html/body/div[7]/div/div[2]/div/div[4]/button[2]")
        _time.sleep(5)
        self._graphQL_id_update()


    





