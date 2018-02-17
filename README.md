# Python 2.x Enumeration Class
Provides an effective, immutable enumeration class with versatile features for python 2.

## Usage

    from Enumeration import Enum

The Enum object takes in a list of strings and generates an immutable, enumerable collection of Enum_Item objects.

    >>> enum_object = Enum (["item1", "item2", ...])

Once set, an enumeration can be referenced by parameters or dictionary reference, and are case insensitive.

    >>> enum_object.item1
    <Enum_Item object at 0x028E3630>
    >>> enum_object["item2"]
    <Enum_Item object at 0x028E3730>
    >>> enum_object.ITEM2
    <Enum_Item object at 0x028E3730>

Each Enum_Item is guaranteed to be unique as each item is a distinct object in memory and will not compare equal with anything other than itself.

    >>> enum_object.item1 == "item1"
    False
    >>> enum_object.item1 == enum_object.item2
    False
    >>> enum_object.item1 == enum_object["item1"]
    True

Attempting to set values in an enumeration after its creation will throw an error.

    >>> enum_object.item1 = "foo"
    TypeError: 'Enum' object does not support attribute assignment
    >>> enum_object["item1"] = "foo"
    TypeError: 'Enum' object does not support item assignment

Each item in the enumeration can return its name with the `name` attribute.

    >>> enum_object.item1.name
    'item1'

Optionally, an Enum can have an internal name set on it at initialisation by supplying a `name` attribute.

    >>> enum_object = Enum (["item1", "item2", ...], name="foobar")

When set, the name of the enumeration can be recalled through the use of the `__name__` method. The enumeration object's name can also be referenced via an Enum_Item object's `type` attribute.

If no name is set, then `__name__` and `type` each return `None`.

    >>> enum_object.__name__()
    'foobar'
    >>> enum_object.item1.type
    'foobar'

Casting an Enum_Item to `str` also differs on whether or not a `name` was set.

    >>> str(enum_object.item1)
    # Without a name set
    'item1'
    # With a name set
    'foobar.item1'

Enum object's can also be iterated over. Note however that order is not preserved, and so the Enum_Item objects are returned in an arbitrary, unknown order.

    >>> for item in enum_object:
            print(item)
    item2
    item1
    ...    # And so on
