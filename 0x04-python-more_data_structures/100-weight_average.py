#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    sum_score = sum(score * weight for score, weight in my_list)
    sum_weight = sum(weight for _, weight in my_list)
    return sum_score / sum_weight if sum_weight else 0

