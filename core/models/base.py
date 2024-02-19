#!/usr/bin/python3
""" Base model """
from uuid import uuid4
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

BaseDB = declarative_base()


class Base:
    """ Baes Class """

    id = Column(Integer, primary_key=True, autoincrement=True)
    u_id = Column(String(36), unique=True, default=uuid4().hex)
    created_at = Column(DateTime(timezone=True), default=datetime.now())
    updated_at = Column(DateTime(timezone=True), default=datetime.now(), onupdate=datetime.now())

    def __init__(self, **kwargs):
        """ Initialize """
        if kwargs:
            for key, val in kwargs.items():
                setattr(self, key, val)
        else:
            self.u_id = uuid4().hex
            self.created_at = datetime.now()
            self.created_at = datetime.now()


    def to_dict(self):
        """ turn the instance to dictionary """
        dictionary = self.__dict__.copy()
        if '_sa_instance_state' in dictionary:
            del dictionary['_sa_instance_state']

        return dictionary


    def __str__(self):
        """ return upon intance call """
        return f"{self.__class__.__name__}: {self.u_id}"
