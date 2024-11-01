def type_eq_str(obj):

    match obj:
        case str() :
            return True
        case _:
            return False
        