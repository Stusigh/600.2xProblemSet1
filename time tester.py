''' a slight modification of Kiwi's speed tester
 times greedy
  and prints the result for each students code'''

import random
import string
from timeit import timeit
from collections import namedtuple, deque
Cow = namedtuple("Cow", "weight name")


# students code


def stu_transport(cows,limit=10):
    
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

def load_cows(filename):

    cow_dict = dict()

    f = open(filename, 'r')

    for line in f:
        line_data = line.split(',')
        cow_dict[line_data[0]] = int(line_data[1])

    return cow_dict


def create_random_test(limit, lengh):
    '''a random cow dict'''
    cows = {"Cow"+str(i): random.randrange(1, limit) for i in range(lengh)}
    return cows


RANDOM_TEST_LIST = create_random_test(10, 100)
PSET_TESTS = load_cows("ps1_cow_data.txt")

def pset_tester(f):
    return f(PSET_TESTS, 10)

def random_tester(f, limit = 10):
    return f(RANDOM_TEST_LIST, 10)

from bisect import insort
for test_fn in ('pset_tester', 'random_tester'):
    times = []
    for fn in ['stu_transport']:
        n = 100000 # just change n to 100 after testing pset-dict, it takes too long on 100 dict
      
        insort(times, (timeit(f'{test_fn}({fn})', globals=globals(), number=n), f'{test_fn} {fn}'))
        
    for element in times:
        print (element)
    print()
