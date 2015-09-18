__author__ = '804'

not_diller_ron = [[1000, 1000, 1300, 1600, 2000, 2300, 2600],
              [1300, 2000, 2600, 3200, 3900, 4500, 5200],
              [2600, 3900, 5200, 6400, 7700, 8000, 8000],
              [5200, 7700, 8000, 8000, 8000, 8000, 8000]]

not_diller_tsumo = [[[500, 300], [500, 300], [700, 400], [800, 400], [1000, 500], [1200, 600], [1300, 700]],
              [[700, 400], [1000, 500], [1300, 700], [1600, 800], [2000, 1000], [2300, 1200], [2600, 1300]],
              [[1300, 700], [2000, 1000], [2600, 1300], [3200, 1600], [3900, 2000], [4000, 2000], [4000, 2000]],
              [[2600, 1300], [3900, 2000], [4000, 2000], [4000, 2000], [4000, 2000], [4000, 2000], [4000, 2000]]]

diller_ron = [[1500, 1500, 2000, 2400, 2900, 3400, 3900],
              [2000, 2900, 3900, 4800, 5800, 6800, 7700],
              [3900, 5800, 7700, 9600, 11600, 12000, 12000],
              [7700, 11600, 12000, 12000, 12000, 12000, 12000]]

diller_tsumo = [[500, 500, 500, 800, 1000, 1200, 1300],
              [700, 1000, 1300, 1600, 2000, 2300, 2600],
              [1300, 2000, 2600, 3200, 3900, 4000, 4000],
              [2600, 3900, 4000, 4000, 4000, 4000, 4000]]

limits = [8000, 12000, 12000, 16000, 16000, 16000, 16000, 24000, 24000]


def calculate_limit(han, is_diller, renchan, tsumo):
    if tsumo:
        if is_diller:
            if han > 12:
                return 16000
            else:
                return int(limits[han - 5]/2) + renchan*100
        else:
            if han > 12:
                return [16000, 8000]
            else:
                return [int(limits[han - 5]/2) + renchan*100, int(limits[han - 6]/4) + renchan*100]
    else:
        if is_diller:
            if han > 12:
                return 48000
            else:
                return int(limits[han - 5]*1.5) + renchan*300
        else:
            if han > 12:
                return 36000
            else:
                return int(limits[han - 5]) + renchan*300

def calculate_not_limit(han, fu, is_diller, renchan, tsumo):
    fu = fu_round(fu)
    if tsumo:
        if is_diller:
            return diller_tsumo[han - 1][int(fu/10) - 2] + renchan*100
        else:
            return [not_diller_tsumo[han - 1][int(fu/10) - 2][0] + renchan*100, not_diller_tsumo[han - 1][int(fu/10) - 2][1] + renchan*100]
    else:
        if is_diller:
            return diller_ron[han - 1][int(fu/10) - 2] + renchan*300
        else:
            return not_diller_ron[han - 1][int(fu/10) - 2] + renchan*300

def fu_round(fu):
    while fu % 10 != 0:
        fu += 1
    return fu
