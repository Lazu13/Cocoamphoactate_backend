#!/usr/bin/env python
# encoding utf-8

from ..models import User, Game, Friends, Score

__all__ = ['Engine', 'ALL_USERS', 'FRIENDS_ONLY']

ALL_USERS = 0
FRIENDS_ONLY = 1


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
        rtype = int(rtype)
        if rtype not in [ALL_USERS, FRIENDS_ONLY]:
            raise ValueError("Not existing type of recommendation")
        self.__type = rtype

    @property
    def user(self):
        return self.__user

    @user.setter
    def user(self, user):
        if not isinstance(user, int):
            raise TypeError("Bad user.id type")
        if user < 1:
            raise ValueError("Not possible userID")
        self.__user = user

    def set_type(self, rtype=ALL_USERS):
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

    @classmethod
    def get_most_popular(cls):
        """
        Method used for getting recommendations of most popular items
        :return: list of game objects
        """
        import operator
        from django.db.models import Avg
        games = Game.objects.all()
        grd = {}
        for game in games:
            scores = list(Score.objects.values('game_id').filter(game_id=game.id).annotate(Avg('score')))
            if len(scores) != 1:
                continue
            idn = scores[0]['game_id']
            avg = scores[0]['score__avg']
            grd.update({idn: avg})

        sorted_grd = sorted(grd.items(), key=operator.itemgetter(1), reverse=True)
        sorted_grd = sorted_grd[:3]
        return sorted_grd

    def get_best_matching(self):
        """
        Method used for getting recommedations using collaborative filtering based on all users or only frieds depending on type parameter
        :return: dictionary of recommended games
        """
        from django.db.models import Q, Avg
        import copy
        import operator
        if self.user is None:
            raise User.DoesNotExist
        users = User.objects.all()
        if self.type == FRIENDS_ONLY:
            friends = Friends.objects.filter(Q(user_one_id=self.user) | Q(user_two_id=self.user))
            if len(friends) > 2:
                users = users.filter(Q(id=friends.values('user_one_id')) | Q(id=friends.values('user_two_id')))

        user_sims = {}
        prefs = {}
        for user in users:
            tab = {}
            scores = Score.objects.values('game_id', 'score').filter(user_id=user)
            for score in scores:
                tab.update({score['game_id']: score['score']})
            prefs.update({copy.deepcopy(user.id): copy.deepcopy(tab)})

        for user in users:
            sim = self.pearson(prefs, self.user, user.id)
            user_sims.update({user.id: sim})

        print(user_sims)
        del user_sims[self.user] # deletion of user for whom the analysis is beeing performed
        user_sims = sorted(user_sims.items(), key=operator.itemgetter(1), reverse=True) # dictionary containing user_ids and users' similarities
        if len(user_sims) < 3:
            return self.get_most_popular()

        games_f = Score.objects.values('game_id', 'score').filter(user_id=user_sims[0][0]).order_by('-score')[:3]
        games_s = Score.objects.values('game_id', 'score').filter(user_id=user_sims[1][0]).order_by('-score')[:3]

        recommended_games = {}
        grd = {}
        games_f_dict = dict([(g['game_id'], g['score']) for g in games_f])
        recommended_games.update(dict(sorted(games_f_dict.items(), key=operator.itemgetter(1), reverse=True)))

        games_s_dict = dict([(g['game_id'], g['score']) for g in games_s])
        recommended_games.update(dict(sorted(games_s_dict.items(), key=operator.itemgetter(1), reverse=True)))

        for game in recommended_games:
            scores = list(Score.objects.values('game_id').filter(game_id=game).annotate(Avg('score')))
            idn = scores[0]['game_id']
            avg = scores[0]['score__avg']
            grd.update({idn: avg})

        return grd

    @classmethod
    def pearson(cls, prefs, p1, p2):
        """
        Pearson algorithm for finding a person who has similar taste.
        :param prefs: dictionary of preferences of people
        :param p1: first person
        :param p2: second person
        :return: float similarity of people
        """
        from math import sqrt
        si = {}
        for item in prefs[p1]:
            if item in prefs[p2]:
                si[item] = 1

        n = float(len(si))

        if n == 0:
            return 0

        sum1 = sum([prefs[p1][it] for it in si])
        sum2 = sum([prefs[p2][it] for it in si])
        sqsum1 = sum([pow(prefs[p1][it], 2) for it in si])
        sqsum2 = sum([pow(prefs[p2][it], 2) for it in si])
        psum = sum([prefs[p1][it] * prefs[p2][it] for it in si])

        num = psum - (sum1 * sum2 / n)
        den = sqrt((sqsum1 - pow(sum1, 2) / n) * (sqsum2 - pow(sum2, 2) / n))
        if den == 0:
            return 0

        r = num / den
        return r
