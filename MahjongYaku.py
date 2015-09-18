# coding=utf-8
from MahjongSet import MahjongSet
import sys

__author__ = '804'


# является ли рука читоицу
def is_chitoitsu(hand):
    if len(hand) % 2 != 0:
        return False
    index = 0
    have_yet = []
    while index != len(hand):
        if (hand[index] != hand[index + 1]) or (hand[index] in have_yet):
            return False
        index += 2
        have_yet.append(hand[index])
    return True


# является ли рука кокущи
def is_kokushimuso(hand):
    terminals_and_honors = [0, 8, 9, 17, 18] + range(26, 33)
    if all(tile in terminals_and_honors for tile in hand) and all(tile in hand for tile in terminals_and_honors):
        return True
    else:
        return False


# проверка руки на таняо
def is_tanyao(hand):
    return all(tile in (range(1, 8) + range(10, 17) + range(19, 26)) for tile in hand)


# проверка руки на якухай (нужен обработчик исключения)
def yakuhai_quantity(set_hand, round_wind, place_wind):
    if round_wind not in range(27, 31):
        raise Exception('Input Error', "Incorrect tile is inputted as round's wind")
    if place_wind not in range(27, 31):
        raise Exception('Input Error', "Incorrect tile is inputted as player's wind")
    yakuhai_count = 0
    for mset in set_hand:
        if mset.set_tile in ([place_wind] + range(31, 34)):
            yakuhai_count += 1
        if mset.set_tile == round_wind:
            yakuhai_count += 1
    return yakuhai_count


# проверка руки на сёсанген
def is_sesangen(set_hand):
    return all(tile in [mset.set_tile for mset in set_hand] for tile in range(31, 34)) and any(
        (mset.name == 'pare') and (mset.set_tile in range(31, 34)) for mset in set_hand)


# проверка руки на пинфу (если тайл победы не входит в руку, то метод возвращает False)
def is_pinfu(chand, wt, round_wind, place_wind):
    return (len(chand) == 5) and all(mset.name in ('chi', 'pare') for mset in chand) and any(
        (mset.name == 'pare') and (mset.set_tile not in (range(31, 34) + [round_wind, place_wind])) for mset in
        chand) and any(
        (mset.name == 'chi') and ((mset.set_tile == wt) or (mset.set_tile + 2 == wt)) for mset in chand)


# проверка руки на чанту
def is_chanta(set_hand):
    return all(
        ((mset.name in ('pon', 'kan', 'pare')) and (mset.set_tile in ([0, 8, 9, 17, 18] + range(26, 34)))) or (
            (mset.name == 'chi') and (mset.set_tile in [0, 6, 9, 15, 18, 24])) for mset in set_hand)


# проверка руки на джунчан
def is_dzhunchan(set_hand):
    return all(((mset.name in ('pon', 'kan', 'pare')) and (mset.set_tile in [0, 8, 9, 17, 18, 26])) or (
        (mset.name == 'chi') and (mset.set_tile in [0, 6, 9, 15, 18, 24])) for mset in set_hand)


# проверка руки на иппейко (только в закрытой руке)
def is_ippeiko(chand):
    for index in range(len(chand)):
        if (chand[index].name == 'chi') and any(
                        (mset.name == 'chi') and (chand[index].set_tile == mset.set_tile) for mset in
                        (chand[:index] + chand[index + 1:])):
            return True
    return False


# проверка руки на рянпейко (только в закрытой руке)
def is_ryanpeiko(chand):
    for first_index in range(len(chand)):
        if chand[first_index].name == 'chi':
            for second_index in range(first_index + 1, len(chand)):
                if (chand[second_index].name == 'chi') and (
                            chand[first_index].set_tile == chand[second_index].set_tile):
                    return is_ippeiko(chand[first_index + 1:second_index] + chand[second_index + 1:])
    return False


# проверка руки на иццу
def is_itsu(set_hand):
    tuple_structure = []
    for mset in set_hand:
        tuple_structure.append((mset.name, mset.set_tile))
    if (('chi', 0) in tuple_structure) and (('chi', 3) in tuple_structure) and (('chi', 6) in tuple_structure):
        return True
    if (('chi', 9) in tuple_structure) and (('chi', 12) in tuple_structure) and (('chi', 15) in tuple_structure):
        return True
    if (('chi', 18) in tuple_structure) and (('chi', 21) in tuple_structure) and (('chi', 24) in tuple_structure):
        return True
    return False


# проверка руки на хоницу
def is_honitsu(hand):
    return all(tile in (range(9) + range(27, 34)) for tile in hand) or all(
        tile in (range(9, 18) + range(27, 34)) for tile in hand) or all(tile in (range(18, 34)) for tile in hand)


# проверка руки на чиницу
def is_chinitsu(hand):
    return all(tile in range(9) for tile in hand) or all(
        tile in range(9, 18) for tile in hand) or all(tile in (range(18, 27)) for tile in hand)


# проверка руки на тойтой
def is_toitoi(set_hand):
    return all(mset.name != 'chi' for mset in set_hand)


# проверка руки на сананко (подается именно закрытая рука)
def is_sananko(chand):
    quantity = 0
    for mset in chand:
        if mset.name == 'pon':
            quantity += 1
        if quantity == 3:
            return True
    return False


# проверка руки на саншоку(содержит обработчик исключений)
# TODO узнать, как сделать класс невидимым для внешних вызовов
def __is_sanshoku(set_hand, set_name):
    try:
        if set_name not in ('pon', 'chi'):
            raise Exception('Argument error',
                            "Function '__is_sanshoku' has been called with incorrect parameter 'set_name'")
    except Exception as e:
        print e[0] + ': ' + e[1]
        sys.exit(0)
    tuple_structure = []
    if set_name == 'pon':
        limit = 9
    else:
        limit = 7
    for mset in set_hand:
        tuple_structure.append((mset.name, mset.set_tile))
    for index in range(limit):
        if ((set_name, index) in tuple_structure) and ((set_name, index + 9) in tuple_structure) and (
                    (set_name, index + 18) in tuple_structure):
            return True
    return False


# проверка руки на саншоку (доджун)
def is_sanshoku_dodjun(set_hand):
    return __is_sanshoku(set_hand, 'chi')


# проверка руки на саншоку доко
def is_sanshoku_doko(set_hand):
    return __is_sanshoku(set_hand, 'pon')


# проверка руки на хонрото (не сочетается с чантой)
def is_honroto(hand):
    return all(tile in ([0, 8, 9, 17, 18] + range(26, 34)) for tile in hand)


# проверка руки на санканцу
def is_sankatsu(set_hand):
    quantity = 0
    for index in range(len(set_hand)):
        if set_hand[index].name == 'kan':
            quantity += 1
        if quantity == 3:
            return True
    return False


# подсчет возможных структур руки с повторениями (убраны лишние строки)
def calc_structure_unfiltered(hand, kan_quantity):
    if kan_quantity != 0:
        index = 0
        structure = []
        while index < len(hand) - 3:

            if all(hand[index + indent] == hand[index + indent + 1] for indent in range(3)):
                branches = calc_structure_unfiltered(hand[:index] + hand[index + 4:], kan_quantity - 1)
                if branches is not None:
                    for branch in branches:
                        branch.append(MahjongSet('kan', hand[index]))
                    structure += branches
                index += 4
            elif hand[index] == hand[index + 2]:
                index += 3
            elif hand[index] == hand[index + 1]:
                index += 2
            else:
                index += 1

        if structure:
            return structure
        else:
            return None

    elif (len(hand) == 2) and (hand[0] == hand[1]):
        return [[MahjongSet('pare', hand[0])]]

    else:
        if len(hand) < 5:
            return None

        index = 0
        structure = []
        while index < len(hand) - 2:

            if all(hand[index + indent] == hand[index + indent + 1] for indent in range(2)):
                branches = calc_structure_unfiltered(hand[:index] + hand[index + 3:], kan_quantity)
                if branches is not None:
                    for branch in branches:
                        branch.append(MahjongSet('pon', hand[index]))
                    structure += branches
                index += 2

            elif hand[index] in (range(0, 6) + range(9, 15) + range(18, 24)):
                if ((hand[index] + 1) in hand) and ((hand[index] + 2) in hand):
                    branches = calc_structure_unfiltered(
                        hand[:index] + hand[index + 1:hand.index(hand[index] + 1)] + hand[hand.index(
                            hand[index] + 1) + 1:hand.index(hand[index] + 2)] + hand[
                                                                                hand.index(hand[index] + 2) + 1:],
                        kan_quantity)
                    if branches is not None:
                        for branch in branches:
                            branch.append(MahjongSet('chi', hand[index]))
                        structure += branches
                index += 1

        if structure:
            return structure
        else:
            return None


# фильтр структур рук: удаление повторяющихся и упорядочивание оставшихся
def calc_structure(hand, kan_quantity):
    structures = calc_structure_unfiltered(hand, kan_quantity)
    string_structures = []
    for structure in structures[:]:
        string_structure_list = []
        structure.sort()
        for mset in structure:
            string_structure_list.append(str(mset))
        string_structure = ','.join(string_structure_list)
        if any(string_structure == str_struct for str_struct in string_structures):
            structures.remove(structure)
        else:
            string_structures.append(string_structure)
    return structures


# TODO проверка руки на Дайсанген
# TODO проверка руки на Шосуши
# TODO проверка руки на Дайсуши
# TODO проверка руки на Тсуисо
# TODO проверка руки на Суанко
# TODO проверка руки на Суанко танки
# TODO проверка руки на Чуренпото
# TODO проверка руки на Одинарный чуренпото
# TODO проверка руки на Рюисоу
# TODO проверка руки на Суканцу
# TODO проверка руки на Чинрото
# TODO проверка руки на Казое якуман

# TODO подсчет минипоинтов
# TODO проработка руки на возможность стакаться с малыми драконами
########################################################################

# является ли ожидание 13-сторонним (не обязательная в данной задаче)
def is_thirteen_sided(hand, wt):
    if is_kokushimuso(hand):
        return kokushimuso_is_thirteen_sided(hand, wt)
    else:
        return False


# является ли кокущи 13-сторонним
def kokushimuso_is_thirteen_sided(hand, wt):
    return wt in (hand[:hand.index(wt)] + hand[hand.index(wt) + 1:])

# TODO реализовать заглушки для подачи открытой, закрытой руки и тайла победы)
