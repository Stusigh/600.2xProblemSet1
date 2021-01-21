# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 07:28:13 2020

@author: stuar
"""
from ps1_partition import get_partitions
cows = {'Buttercup': 72, 'Daisy': 50, 'Betsy': 65}
limit=75


def ship_weight(cow_list, cow_dict):
    '''
    given a cow dictionary and a cow trip, gives you the total weight of the 
    cows on that trip. Returns an integer
    '''
    weight = 0
    for cow in cow_list:
        weight += cow_dict[cow]
    return weight
        



best_combo_len = len(cows)

for combo in (get_partitions(cows)):
    valid_combo = True
    for trip in combo:
        trip_weight = ship_weight(trip, cows)
        if trip_weight > limit:
            valid_combo = False
    if valid_combo == True:
        if len(combo) <= best_combo_len:
            best_combo = combo
            best_combo_len = len(combo)

