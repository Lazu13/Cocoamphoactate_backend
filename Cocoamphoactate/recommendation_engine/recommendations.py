#!/usr/bin/env python
# encoding utf-8

from ..models import User, Game, GameLib, Friends


__all__ = ['Engine', 'ALL_USERS', 'FRIENDS_ONLY']

ALL_USERS = 1
FRIENDS_ONLY = 2


class Engine(object):
    """
    Class used for getting recomendations for specified user.
    It may return either most popular items or items based on friends/all users' opinions and interests of the user.
    """
    def __init__(self):
        """Initializator for class Engine"""
        self.__type = ALL_USERS
        self.__user = None

    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, rtype):
        if rtype not in [ALL_USERS, FRIENDS_ONLY]:
            raise ValueError("Not existing type of recommendation")
        self.__type = rtype

    @property
    def user(self):
        return self.__user

    @user.setter
    def user(self, user):
        if user.id < 0:
            raise ValueError("Not possible userID")
        self.__user = user

    def set_type(self, rtype = ALL_USERS):
        """
        Setter used for setting type of recommendations
        :param type: int [ALL_USERS, FRIENDS_ONLY] - specifies on whom recommendations are based
        """
        self.type = rtype

    def set_user(self, user):
        """
        Setter used for setting a user who will be given recommendations
        :param user:
        """
        self.user = user

    def get_most_popular(self):
        """
        Method used for getting recommendations of most popular items
        :return:
        """
        pass

    def get_best_matching(self):
        """
        Method used for getting recommedations using collaborative filtering based on all users or only frieds depending on type parameter
        :return:
        """
        pass
