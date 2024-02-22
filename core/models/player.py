#!/usr/bin/python3
""" User Module """
from sqlalchemy import Column, String
from core.models.base import Base, BaseDB


class Player(Base, BaseDB):
    """ User class """
    __tablename__ = "players"

    name = Column(String(50))
    won = None


    def __init__(self, p_name, **kwargs):
        super().__init__(**kwargs)
        if p_name:
            self.name = p_name
