__author__ = '804'

import sys


class MahjongSet(object):
    tiles = ['1-man', '2-man', '3-man', '4-man', '5-man', '6-man', '7-man', '8-man', '9-man',
             '1-pin', '2-pin', '3-pin', '4-pin', '5-pin', '6-pin', '7-pin', '8-pin', '9-pin',
             '1-sou', '2-sou', '3-sou', '4-sou', '5-sou', '6-sou', '7-sou', '8-sou', '9-sou',
             'est', 'south', 'west', 'north', 'haku', 'hatsu', 'chun']

    set_list = ('chi', 'pon', 'kan', 'pare')

    def __init__(self, set_name, set_tile):
        try:
            if set_name in self.set_list:
                self.name = set_name
                if (set_name == 'chi') and (set_tile in (range(0, 7) + range(9, 16) + range(18, 25))):
                    self.set_tile = set_tile
                    self.is_correct = True
                elif (set_name in ('pon', 'kan', 'pare')) and (set_tile in range(0, 34)):
                    self.set_tile = set_tile
                    self.is_correct = True
                else:
                    raise Exception("Parameter error", "Incorrect tile is inputed!")
            else:
                raise Exception("Parameter error", "Incorrect set name is inputed")
        except Exception as e:
            print e[0] + ': ' + e[1]
            sys.exit(0)

    def __str__(self):
        if self.name == 'chi':
            return self.name + ' of ' + self.tiles[self.set_tile] + ', ' + self.tiles[self.set_tile + 1] + ', ' + \
                   self.tiles[self.set_tile + 2]
        elif self.name in ('pon', 'kan', 'pare'):
            return self.name + ' of ' + self.tiles[self.set_tile]

    def __cmp__(self, other):
        if self.set_tile < other.set_tile:
            return -1
        elif self.set_tile == other.set_tile:
            if self.name != other.name:
                if self.set_list.index(self.name) < other.set_list.index(other.name):
                    return -1
                else:
                    return 1
            else:
                return 0
        else:
            return 1
