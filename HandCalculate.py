# coding=utf-8
__author__ = '804'

import sys
from MahjongSet import MahjongSet
import MahjongYaku

diller = False
riichi = False
double_riichi = False
ipatsu = False
tsumo = False
rinshan = False
chankan = False
hotei = False
hand = []
tile_count = 0
renchan = 0
dora_indicator = []
dora_pick = False
akadora_count = 0
min_number_of_tiles = 14
tiles = ['1-man', '2-man', '3-man', '4-man', '5-man', '6-man', '7-man', '8-man', '9-man',
         '1-pin', '2-pin', '3-pin', '4-pin', '5-pin', '6-pin', '7-pin', '8-pin', '9-pin',
         '1-sou', '2-sou', '3-sou', '4-sou', '5-sou', '6-sou', '7-sou', '8-sou', '9-sou',
         'est', 'south', 'west', 'north', 'haku', 'hatsu', 'chun']

option_keys = ['-r', '-d', '-tsu', '-rin', '-cha', '-h']
open_hand = []

""" 1-man - 0       1-pin - 9       1-sou - 18      est - 27
    2-man - 1       2-pin - 10      2-sou - 19      south - 28
    3-man - 2       3-pin - 11      3-sou - 20      west - 29
    4-man - 3       4-pin - 12      4-sou - 21      north - 30
    5-man - 4       5-pin - 13      5-sou - 22      haku - 31
    5-man-red - 4   5-pin-red - 13  5-sou-red - 22  hatsu - 32
    6-man - 5       6-pin - 14      6-sou - 23      chun - 33
    7-man - 6       7-pin - 15      7-sou - 24
    8-man - 7       8-pin - 16      8-sou - 25
    9-man - 8       9-pin - 17      9-sou - 26    """

try:
    if '-hand' not in sys.argv:
        raise Exception("Input error", "Have no key '-hand'")
except Exception as e:
    print e[0] + ': ' + e[1]
    sys.exit(0)

try:
    if '-wt' not in sys.argv:
        raise Exception("Input error", "Have no key '-wt'")
except Exception as e:
    print e[0] + ': ' + e[1]
    sys.exit(0)

try:
    if '-chand' not in sys.argv:
        raise Exception("Input error", "Have no key '-chand'")
except Exception as e:
    print e[0] + ': ' + e[1]
    sys.exit(0)

try:
    if '-dora' not in sys.argv:
        raise Exception("Input error", "Have no key '-dora'")
except Exception as e:
    print e[0] + ': ' + e[1]
    sys.exit(0)

if '5-man-red' in sys.argv[1:]:
    akadora_count += 1
    sys.argv[sys.argv.index('5-man-red')] = '5-man'

if '5-pin-red' in sys.argv[1:]:
    akadora_count += 1
    sys.argv[sys.argv.index('5-pin-red')] = '5-pin'

if '5-sou-red' in sys.argv[1:]:
    akadora_count += 1
    sys.argv[sys.argv.index('5-sou-red')] = '5-sou'

argv_index = 1

while argv_index < sys.argv.index('-hand'):

    try:

        if dora_pick:
            if sys.argv[argv_index] in tiles:
                dora_indicator.append(tiles.index(sys.argv[argv_index]))
                argv_index += 1
                if len(dora_indicator) > 10:
                    raise Exception("Input error", "Incorrect quantity of parameters after key '-dora")
                continue
            else:
                if not dora_indicator:
                    raise Exception("Input error", "Incorrect parameter after key '-dora")
                else:
                    dora_pick = False
                    continue

        if sys.argv[argv_index] == '-d':
            if not diller:
                diller = True
                argv_index += 1
                continue
            else:
                raise Exception("Input Error", "Duplicate key '-d'")

        if sys.argv[argv_index] == '-rin':
            if int(sys.argv[argv_index + 1]) == 0:
                renchan = int(sys.argv[argv_index + 1])
                argv_index += 2
                continue
            else:
                raise Exception("Input Error", "Duplicate key '-ren'")

        if sys.argv[argv_index] == '-ri':
            if not riichi:
                if int(sys.argv[argv_index + 1]) in range(4):
                    riichi = True
                    if int(sys.argv[argv_index + 1]) % 2:
                        double_riichi = True
                    if int(sys.argv[argv_index + 1]) // 2:
                        ipatsu = True
                else:
                    raise Exception("Input Error", "Incorrect parameter after key '-ri'")
                argv_index += 2
                continue
            else:
                raise Exception("Input Error", "Duplicate key '-ri'")

        if sys.argv[argv_index] == '-tsu':
            if not tsumo:
                tsumo = True
                argv_index += 1
                continue
            else:
                raise Exception("Input Error", "Duplicate key '-tsu'")

        if sys.argv[argv_index] == '-rin':
            if not rinshan:
                rinshan = True
                min_number_of_tiles += 1
                argv_index += 1
                if '-tsu' not in sys.argv[1:sys.argv.index('-hand')]:
                    raise Exception("Key error", "Key '-rin' can't to be inputed without key '-tsu'")
                if ('-cha' in sys.argv[1:sys.argv.index('-hand')]) or ('-h' in sys.argv[1:sys.argv.index('-hand')]):
                    raise Exception("Key error", "Only one of the keys '-rin', '-cha', '-h' can be specified")
                continue
            else:
                raise Exception("Input Error", "Duplicate key '-rin'")
        elif sys.argv[argv_index] == '-cha':
            if not chankan:
                chankan = True
                argv_index += 1
                if '-h' in sys.argv[1:sys.argv.index('-hand')]:
                    raise Exception("Key error", "Only one of the keys '-rin', '-cha', '-h' can be specified")
                if '-tsu' in sys.argv[1:sys.argv.index('-hand')]:
                    raise Exception("Key error", "Key '-cha' can't to be inputed with key '-tsu'")
                continue
            else:
                raise Exception("Input Error", "Duplicate key '-cha'")
        elif sys.argv[argv_index] == '-h':
            if not hotei:
                hotei = True
                argv_index += 1
                if '-tsu' not in sys.argv[1:sys.argv.index('-hand')]:
                    raise Exception("Key error", "Key '-h' can't to be inputed without key '-tsu'")
                continue
            else:
                raise Exception("Input Error", "Duplicate key '-h'")

        if sys.argv[argv_index] == '-dora':
            if not dora_indicator:
                dora_pick = True
                argv_index += 1
                continue
            else:
                raise Exception("Input Error", "Duplicate key '-dora'")

        raise Exception("Input error", "Incorrect parameters before key '-hand'")

    except Exception as e:
        print e[0] + ': ' + e[1]
        sys.exit(0)

try:
    if '-ohand' in sys.argv[sys.argv.index('-hand'):]:
        if not ((sys.argv.index('-hand') < sys.argv.index('-wt')) and (
                    sys.argv.index('-wt') < sys.argv.index('-ohand')) and (
                    sys.argv.index('-ohand') < sys.argv.index('-chand'))):
            raise Exception("Input error", "Incorrect input order")
        else:
            if sys.argv[sys.argv.index('-hand'):].count('-ohand') != 1:
                raise Exception("Input Error", "Duplicate key '-ohand'")

            if sys.argv.index('-ohand') - sys.argv.index('-wt') > 2:
                raise Exception("Input error", "Incorrect parameter(-s) before key '-chand'")

            # обработка открытой руки
            argv_index = sys.argv.index('-ohand') + 1
            while argv_index < sys.argv.index('-chand'):
                if sys.argv[argv_index] == '-chi':
                    if (tiles.index(sys.argv[argv_index + 1]) in (range(0, 7) + range(9, 16) + range(18, 25))) and (
                                tiles.index(sys.argv[argv_index + 2]) == tiles.index(
                                sys.argv[argv_index + 1]) + 1) and (
                                tiles.index(sys.argv[argv_index + 3]) == tiles.index(sys.argv[argv_index + 1]) + 2):
                        open_hand.append(MahjongSet('chi', tiles.index(sys.argv[argv_index + 1])))
                        hand.append(tiles.index(sys.argv[argv_index + 1]))
                        hand.append(1 + tiles.index(sys.argv[argv_index + 1]))
                        hand.append(2 + tiles.index(sys.argv[argv_index + 1]))
                        tile_count += 3
                        argv_index += 4
                        continue
                    else:
                        raise Exception("Input error", "Incorrect set indificators after key '-chi'")
                elif sys.argv[argv_index] == '-pon':
                    if tiles.index(sys.argv[argv_index + 1]) in range(0, 34):
                        open_hand.append(MahjongSet('pon', tiles.index(sys.argv[argv_index + 1])))
                        hand.append(tiles.index(sys.argv[argv_index + 1]))
                        hand.append(tiles.index(sys.argv[argv_index + 1]))
                        hand.append(tiles.index(sys.argv[argv_index + 1]))
                        tile_count += 3
                        argv_index += 2
                        continue
                    else:
                        raise Exception("Input error", "Incorrect set indificator after key '-pon'")
                elif sys.argv[argv_index] == '-kan':
                    if tiles.index(sys.argv[argv_index + 1]) in range(0, 34):
                        open_hand.append(MahjongSet('kan', tiles.index(sys.argv[argv_index + 1])))
                        hand.append(tiles.index(sys.argv[argv_index + 1]))
                        hand.append(tiles.index(sys.argv[argv_index + 1]))
                        hand.append(tiles.index(sys.argv[argv_index + 1]))
                        hand.append(tiles.index(sys.argv[argv_index + 1]))
                        tile_count += 4
                        argv_index += 2
                        continue
                    else:
                        raise Exception("Input error", "Incorrect set indificator after key '-kan'")

                raise Exception("Input error", "Incorrect open hand's input")


    else:
        if not (
                    (sys.argv.index('-hand') < sys.argv.index('-wt')) and (
                            sys.argv.index('-wt') < sys.argv.index('-chand'))):
            raise Exception("Input error", "Incorrect input order")

        if sys.argv.index('-chand') - sys.argv.index('-wt') > 2:
            raise Exception("Input error", "Incorrect parameter(-s) before key '-chand'")

    if sys.argv[sys.argv.index('-hand'):].count('-hand') != 1:
        raise Exception("Input Error", "Duplicate key '-hand'")

    if sys.argv[sys.argv.index('-hand'):].count('-wt') != 1:
        raise Exception("Input Error", "Duplicate key '-wt'")

    if sys.argv[sys.argv.index('-hand'):].count('-chand') != 1:
        raise Exception("Input Error", "Duplicate key '-chand'")

    if sys.argv.index('-wt') - sys.argv.index('-hand') > 1:
        raise Exception("Input error", "Incorrect parameter(-s) before key '-wt'")

    if sys.argv[sys.argv.index('-wt') + 1] not in tiles:
        raise Exception("Input error", "Incorrect parameter after key '-wt'")

except Exception as e:
    print e[0] + ': ' + e[1]
    sys.exit(0)

win_tile = tiles.index(sys.argv[sys.argv.index('-wt') + 1])
hand.append(win_tile)
tile_count += 1

try:
    for tile in sys.argv[sys.argv.index('-chand') + 1:]:
        tile_count += 1
        if tile in tiles:
            hand.append(tiles.index(tile))
        else:
            raise Exception("Input error", "Incorrect parameters after key '-chand'")
except Exception as e:
    print e[0] + ': ' + e[1]
    sys.exit(0)

# Счет тайлов в руке!

try:
    if tile_count < min_number_of_tiles:
        raise Exception("Input error", "Not enought tiles in hand (parameters after key '-chand'/'ohand')")
except Exception as e:
    print e[0] + ': ' + e[1]
    sys.exit(0)

hand.sort()

# TODO посчитать количество тайлов в руке и ограничить до 18
# TODO ограничить количество каждого тайла до 4
# TODO без наличия кана невозможен риншан
# TODO посчитать количество канов
# TODO добавить ветер раунда и ветер места, как входной параметр
# TODO добавить обработку тайла победы в зависимости от того, как завершена игра: по рону или цумо. Если по рону, то сет с ним идет в открытую руку. Если по цумо, то в закрытую.
#  код проверки неструктурных яку и формирования структуры

# отладка!!!
print "Open hand:"
print [str(set) for set in open_hand]

print "\nHand:"
print [tiles[tile] for tile in hand]

print "\nWin Tile: %s\n" % tiles[win_tile]

print "Dora list:"
print [tiles[dora] for dora in dora_indicator]

print "\nAkadoras: %d" % akadora_count

print "\nDiller = %s" % diller
print "Renchan = %d" % renchan
print "Riichi = %s" % riichi
print "\tDouble Riichi = %s" % riichi
print "\tIpatsu = %s" % riichi
print "Tsumo = %s" % tsumo
print "Rinshan = %s" % rinshan
print "Chankan = %s" % chankan
print "Hotei = %s" % hotei
