import operator
import heapq
import os


class ParseLog(object):
    """

    """

    def __init__(self, path):
        """

        :param path:
        :return:
        """
        self.game_log = open(os.path.join(path, "game.log"))
        self.combat_log = open(os.path.join(path, "combat.log"))
        decorated = []
        for f in [self.game_log, self.combat_log]:
            decorated.append(((l.split()[0], l[:-1]) for l in f if l.strip()))
        self.log_merge = map(operator.itemgetter(-1), heapq.merge(*decorated))

    def __del__(self):
        """

        :return:
        """
        self.game_log.close()
        self.combat_log.close()

    def print_log_merged(self):
        """

        :return:
        """
        for line in self.log_merge:
            print(line)
