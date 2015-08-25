#-----------------------------------------------------------------------
#   Python 2.x Enumeration class
#   Copyright (c) 2015 Nathan Sullivan (email: contact@torrentails.com)
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU Lesser General Public License as
#   published by the Free Software Foundation, either version 3 of the
#   License, or (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#   GNU Lesser General Public License for more details.
#
#   You should have received a copy of the GNU Lesser General Public
#   License along with this program.
#   If not, see http://www.gnu.org/licenses/lgpl
#-----------------------------------------------------------------------

##----------------------------------------------------------------------
##  
##                              Usage
##  
##      >>> from enumeration import *
##  
##  An Enum is an immutable object that takes a sting name as its first
##  parameter and an iterable containing only strings as its second, and
##  returns itself to be assigned to a variable.
##  
##      >>> enum_object = Enum ("enum name", ("item1", "item2", ...))
##  
##  the list/args passed become the enumerations items and can be
##  referenced by parameters or dictionary item reference, and are case
##  insensitive.
##  
##      >>> enum_object.item1
##      <Enum_Item object at 0x028E3630>
##      >>> enum_object["Item2"]
##      <Enum_Item object at 0x028E3730>
##  
##  Each Enum item is guaranteed to be unique as each item is an object
##  in memory and will not compare equal with anything other than itself
##  
##      >>> enum_object.item1 == "item1"
##      False
##      >>> enum_object.item1 == enum_object.item2
##      False
##      >>> enum_object.item1 == enum_object["item1"]
##      True
##  
##  Attempting to set values in an enumeration after its creation will
##  throw an error
##  
##      >>> enum_object.item1 = "Foo"
##      TypeError: 'Enum' object does not support attribute assignment
##      >>> enum_object["item1"] = "Foo"
##      TypeError: 'Enum' object does not support item assignment
##  
##  Each item in the enumeration can return its name with the `name`
##  attribute.
##  
##      >>> enum_object.item1.name
##      'item1'
##  
##  The name of the enumeration object can be recalled through the use
##  of the `__name__` method. The enumeration object's name can also be
##  referenced via an items `type` attribute.
##  
##      >>> enum_object.__name__()
##      'enum name'
##      >>> enum_object.item1.type
##      'enum name'
##
##  Membership and non-membership can be tested
##
##      >>> enum_object.item2 in enum_object
##      True
##      >>> foo = enum_object.item1
##      >>> foo not in enum_object
##      False
##
##----------------------------------------------------------------------

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
        else: raise AttributeError("No such attribute on 'Enum_Item' object.", name)
    def __setattr__(self, name, value):
        if self._initiated:
            raise TypeError("'Enum_Item' object does not support attribute assignment", name, value)
        else: super(Enum_Item, self).__setattr__(name, value)

class Enum(object):
    _d = {}
    _name = ''
    _initiated = False
    def __init__(self, name, enums):
        if type(name) != str: raise ValueError("Invalid name for object 'Enum'", name)
        for i in enums:
            if type(i) != str: raise TypeError("Enum values must be a string.", i)
            if enums.count(i) > 1: raise ValueError("Duplicate values not allowed.", i)
            self._d[i.upper().replace(' ','')] = Enum_Item(i, name)
        self._name = name
        self._initiated = True
    def __getattr__(self, a):
        try:
            return self._d[a.upper()]
        except KeyError:
            raise AttributeError("No enum value defined.", a)
        else:
            raise
    def __setattr__(self, a, v):
        if self._initiated:
            raise TypeError("'Enum' object does not support attribute assignment")
        else: super(Enum, self).__setattr__(a, v)
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