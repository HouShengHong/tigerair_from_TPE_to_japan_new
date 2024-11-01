import datetime as _datetime

def type_eq_date(obj) -> bool:
    """ """
    match obj:
        case _datetime.date():
            return True
        case _ :
            return False

def date_eq_today(date: _datetime.date) -> bool:
    """ """
    match date:
        case _datetime.date.today():
            return True
        case _ :
            return False

def date_gt_today(date: _datetime.date) -> bool :
    """ """
    match date:
        case d if type_eq_date(d):
            match d:
                case d if d > _datetime.date.today():
                    return True
                case _ :
                    return False
        case _:
            return False

                
    
def date_ge_today(date: _datetime.date) -> bool :
    """ """
    match date:
        case d if type_eq_date(d):
            match d:
                case d if d >= _datetime.date.today():
                    return True
                case _ :
                    return False
        case _:
            return False
        