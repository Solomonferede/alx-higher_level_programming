#!/use/bin/python3
"""module 0-lookup
Defin a method lookup
"""


def lookup(obj):
    """Defining lookup function returning the list of atributes of a class

    Args:
        obj - object to look in the atributes and methods
        """

    return dir(obj)
