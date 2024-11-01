class _BaseCommon:
    @classmethod
    def method_all_attrs(cls):
        dic_attrs = {}
        for attr in cls.__dict__:
            if not attr.startswith('__') and not callable(getattr(cls, attr)):
                dic_attrs[attr] = getattr(cls, attr)
        return dic_attrs