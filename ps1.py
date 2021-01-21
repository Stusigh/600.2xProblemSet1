###########################
# 6.00.2x Problem Set 1: Space Cows 

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """

    cow_dict = dict()

    f = open(filename, 'r')
    
    for line in f:
        line_data = line.split(',')
        cow_dict[line_data[0]] = int(line_data[1])
    return cow_dict


# Problem 1
def greedy_cow_transport(cows,limit=10):
    
    def find_heaviest(dict_cows, limit):
        '''given a dictionary of cows and a limit, returns the heaviest cow that
        fits in that limit'''
        copydic = dict_cows.copy()
        heaviest = (None, 0)
        for cow in dict_cows:
            if dict_cows[cow] > heaviest[1]:
                heaviest = cow, dict_cows[cow]
        if heaviest[1] > limit:
            copydic.pop(heaviest[0])
            return find_heaviest(copydic, limit)
        else:
            return heaviest

    all_trips = []
    dict_copy = cows.copy()
    
    
    while len(dict_copy) != 0:            
        trip = []
        limit_copy = limit
        
        while find_heaviest(dict_copy, limit_copy)[0]!= None:
            cow_to_consider = find_heaviest(dict_copy, limit_copy)
            dict_copy.pop(cow_to_consider[0])
            limit_copy -= cow_to_consider[1]
            trip.append(cow_to_consider[0])
            
        all_trips.append(trip)
        
    return all_trips


# Problem 2
def brute_force_cow_transport(cows,limit=10):

    def ship_weight(cow_list, cow_dict):
        '''
        given a cow dictionary and a cow trip, gives you the total weight of the 
        cows on that trip. Returns an integer
        '''
        weight = 0
        for cow in cow_list:
            weight += cow_dict[cow]
        return weight
    
    best_combo=[]
    best_combo_len = len(cows)
    
    for combo in (get_partitions(cows)):
        valid_combo = True
        for trip in combo:
            if ship_weight(trip, cows) > limit:
                valid_combo = False
        if valid_combo == True:
            if len(combo) <= best_combo_len:
                best_combo = combo
                best_combo_len = len(combo)
                
    return best_combo
        
# Problem 3
def compare_cow_transport_algorithms(cows, limit):
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    start = time.time()
    greedy_cow_transport(cows, limit)
    end = time.time()
    print(end - start)
    '''
    ----
    '''
    start = time.time()
    brute_force_cow_transport(cows, limit)
    end = time.time()
    print(end - start)


"""
Here is some test data for you to see the results of your algorithms with. 
Do not submit this along with any of your answers. Uncomment the last two
lines to print the result of your problem.
"""

cows = load_cows('ps1_cow_data.txt')
limit=10

print(greedy_cow_transport(cows, limit))
#print(brute_force_cow_transport(cows, limit))

compare_cow_transport_algorithms(cows, limit)


