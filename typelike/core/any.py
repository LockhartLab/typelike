"""
any.py
written in Python3
author: C. Lockhart <chris@lockhartlab.org>
"""

from abc import ABCMeta

# Contents
__all__ = [
    'AnyLike'
]


# AnyLike class
class AnyLike(metaclass=ABCMeta):
    """
    Anything is ``AnyLike``

    Note: this class is not implemented. Don't create an instance, because it doesn't do anything.
    """

    # Needed to trick PyCharm
    def __init__(self):
        raise NotImplementedError

    # Needed to trick PyCharm
    def __getitem__(self, item):
        raise NotImplementedError

    # Needed to trick PyCharm
    def __iter__(self):
        raise NotImplementedError

    # Needed to trick PyCharm
    def __len__(self):
        raise NotImplementedError

    # Register subclass as ArrayLike
    @classmethod
    def register(cls, subclass):
        """
        Registers a new subclass

        Parameters
        ----------
        subclass : class
            Subclass to register
        """

        # noinspection PyCallByClass
        ABCMeta.register(cls, subclass)


# Register subclasses
# AnyLike.register()
