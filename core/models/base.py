#!/usr/bin/python3
""" Base model """
from uuid import uuid4
from datetime import datetime


class Base:
    """ Baes Class """
    def __init__(self, **kwargs):
        """ Initialize """
        if not kwargs:
            self.id = uuid4()
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            for key, val in kwargs.items():
                setattr(self, key, val)


    def to_dict(self):
        """ turn the instance to dictionary """
        dictionary = self.__dict__.copy()
        return dictionary


    @classmethod
    def __repr__(cls):
        """ return upon intance call """
        return cls.__name__

