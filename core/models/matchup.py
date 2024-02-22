#!/usr/bin/python3
""" Player matching module """
from core.models.base import BaseDB
import random


class MatchUp:
    """ Match making Class """

    __matchs = {}


    def __init__(self, args):
        """ Initialize """
        if args:
            self.make_match(args)


    def make_match(self, args, **kwargs):
        """ Match maker funcion """
        if args and not kwargs:
            if len(args) % 2 != 0:
                single = args[-1]
                args = args[:-1]
            else:
                single = None

            random.shuffle(args)
            pairs = [(args[i], args[i+1]) for i in range(0, len(args), 2)]
            i = 1
            for pair in pairs:
                mName = f"match_{i}"
                self.__matchs.update({mName: pair})
                i += 1
            if single:
                mName = f"match_{i}"
                self.__matchs.update({mName: [single]})



    def rematch(self):
        """ Make match of the exiting winners """
        winners = []
        for p in self.__matchs:
            ps = self.__matchs[p]
            if len(ps) == 2:
                if ps[0].win:
                    winners.append(ps[0])
                else:
                    winners.append(ps[1])


    def get_matchs(self):
        return self.__matchs
