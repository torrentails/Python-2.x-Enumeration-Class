class Enum(object):
    _initiated = False


    class Enum_Item(object):

        _name = ''
        _type = ''
        _initiated = False

        def __init__(self, name, type):
            self._name = name
            self._type = type
            self._initiated = True

        def __getattr__(self, name):
            if name == 'name':
                return self._name
            if name == 'type':
                return self._type
            else:
                raise AttributeError("No such attribute on 'Enum_Item' object.",
                                        name)

        def __setattr__(self, name, value):
            if self._initiated:
                raise TypeError("'Enum_Item' object does not support"
                                "attribute assignment", name, value)
            else: super(self.__class__, self).__setattr__(name, value)

        def __str__(self):
            if self.type:
                return self.type+'.'+self.name
            return self.name


    def __init__(self, enum_items, name=None):
        if name:
            if type(name) != str:
                raise ValueError("Invalid name for object 'Enum'", name)
        self._name = name

        self._d = {}

        for i in enum_items:
            if type(i) != str:
                raise TypeError("Enum values must be a string.", i)
            if enum_items.count(i) > 1:
                raise ValueError("Duplicate values not allowed.", i)

            self._d[i.upper().replace(' ','')] = Enum_Item(i, name)

        self._initiated = True

    def __getattr__(self, a):
        try:
            return self._d[a.upper()]
        except KeyError:
            raise AttributeError("No enum value defined.", a)

    def __setattr__(self, a, v):
        if self._initiated:
            raise TypeError("'Enum' object does not support"
                            "attribute assignment")
        else: super(self.__class__, self).__setattr__(a, v)

    def __getitem__(self, k):
        return self._d[k.upper().replace(' ','')]

    def __name__(self):
        return self._name

    def __iter__(self):
        i = 0
        l = self._d.values()
        while i < len(l):
            yield l[i]
            i+=1
