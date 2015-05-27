# Python 2.x Enumeration Class
Provides an effective enumeration class with versatile features

## Licence
The Enum class is Copyright (c) 2015 Nathan Sullivan of torrentails.com and is licensed under the GNU Lesser General Public License version 3

## Usage

    Enum        ::= "Enum" "(" name "," items ")"
    name        ::= string
    items       ::= item | item_list
    item_list   ::= "[" item "]"
    item        ::= string [("," item)]

An Enum is an object that takes a string name as it's first parameter and either a list of strings or all remaining arguments are strings, and returns itself in order to be assigned to a variable.

    >>> enum_object = Enum ("enum name", ["item1", "item2", ...])
    >>> enum_object = Enum ("enum name", "item1", "item2", ...)

the list/args passed become the enumeration's items and can be referenced by parameters or dictionary item reference, and are case insensitive.

    >>> enum_object.item1
    <Enum_Item object at 0x028E3630>
    >>> enum_object["iTeM2"]
    <Enum_Item object at 0x028E3730>

Each Enum item is guaranteed to be unique as each item is an object in memory and will not compare equal with anything other than itself.

    >>> enum_object.item1 == "item1"
    False
    >>> enum_object.item1 == enum_object.item2
    False
    >>> enum_object.item1 == enum_object["item1"]
    True

Attempting to set values in an enumeration after its creation will throw an error.

    >>> enum_object.item1 = "Foo"
    NotImplementedError: 'Enum' object does not support attribute assignment
    >>> enum_object["item1"] = "Foo"
    TypeError: 'Enum' object does not support item assignment

Each item in the enumeration can return its name with the `name` attribute.

    >>> enum_object.item1.name
    'item1'

The name of the enumeration object can be recalled through the use of the `__name__` method. The enumeration object's name can also be referenced via an item's `type` attribute.

    >>> enum_object.__name__()
    'enum name'
    >>> enum_object.item1.type
    'enum name'