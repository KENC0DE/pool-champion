#!/usr/bin/python3
""" Storage module """
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from core.models.base import BaseDB
from os import getenv
from core.models.player import Player


class Storage:
    """ Storage Class """

    __engine = None
    __session = None


    def __init__(self):
        user = getenv('POOL_USER')
        db = getenv('POOL_DB')
        password = getenv('POOL_PASS')
        host = getenv('POOL_HOST')

        db_path = f"mysql+mysqldb://{user}:{password}@{host}/{db}"
        self.__engine = create_engine(db_path)


    def load(self):
        """ Load the database """
        BaseDB.metadata.create_all(self.__engine)
        make_session = scoped_session(sessionmaker(bind=self.__engine))
        self.__session = make_session()


    def list_all(self, inst=None):
        """ List everything in The storage. """
        if inst:
            all_inst = self.__session.query(inst).all()
        else:
            all_inst = self.__session.query(Player).all()
        
        return all_inst


    def save(self):
        """ Save instance to the storage """
        self.__session.commit()


    def add(self, inst):
        """ Add new instance to the storage """
        if not inst:
            return

        self.__session.add(inst)
