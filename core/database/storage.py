#!/usr/bin/python3
""" Storage module """
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from core.models.base import BaseDB
from os import getenv


class Storage:
    """ Storage Class """

    __engine = None
    __session = None


    def __init__(self):
        user = getenv('POOL_USER')
        db = getenv('POOL_DB')
        password = getenv('POOL_PASS')
        host = getenv('POOL_HOST')

        db_path = f"mysql+mysqlb://{user}:{password}@{host}/{db}"
        self.__engine = create_engine(db_path)


    def load(self):
        """ Load the database """
        BaseDB.metadata.create_all(self.__engine)
        make_session = scoped_session(sessionmaker(bind=self.__engine))
        self.__session = make_session()


    def list_all(self):
        """ List everything in The storage. """
        pass
