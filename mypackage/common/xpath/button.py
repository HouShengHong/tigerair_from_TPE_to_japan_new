from ...common import _BaseCommon

class Button(_BaseCommon):
    language_bar = '/html/body/div[1]/div/div/header/div/div[2]/button[2]'
    language_bar_option_chinese = '/html/body/div[8]/div/div/div[6]'

    currency_bar = '/html/body/div[1]/div/div/header/div/div[2]/button[3]/span[2]/div'
    currency_bar_option_TWD = '/html/body/div[8]/div/div/div[1]'

    round_trip = '/html/body/div[1]/div/div/div/main/div/div/form/div/div[1]/div[1]/div[2]/div[1]/div[1]'

    origin_airport_bar = '/html/body/div[1]/div/div/div/main/div/div/form/div/div[2]/div/div/div/div[1]/div/div/label[1]/div/div'
    origin_airport_bar_option_TPE =             '/html/body/div[8]/div/div/div/div[3]/button'

    destination_airport_bar = '/html/body/div[1]/div/div/div/main/div/div/form/div/div[2]/div/div/div/div[1]/div/div/label[2]/div/div'
    # destination_airport_bar_option_kanto =    '/html/body/div[6]/div/div/div/div[2]/button'

    search = '/html/body/div[1]/div/div/div/main/div/div/form/div/div[3]/div[3]/button'