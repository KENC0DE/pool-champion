#!/usr/bin/python3
""" Player matching module """


class MatchUp:
    """ Match making Class """

    matchs = None


    def __init__(self, **kwargs):
        """ Initialize """
        if not kwargs:
            self.make_match()
        else:
            for key, val in kwargs.items():
                setattr(self, key, val)


    def make_match(self):
        """ Match maker funcion """
        pass
