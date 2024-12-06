import itertools
import random

def make_random(letters):
    random_letters = list(itertools.permutations(letters))
    random.shuffle(random_letters)
    return [''.join(i) for i in random_letters]

def linear_searching_algorithm(random_letters, target):
    for i, n in enumerate(random_list):
        if n == target:
            return i

#start
letters = ['A', 'B', 'C', 'D']
random_list = make_random(letters)
print('Random List:', random_list)

random_search = random.choice(random_list)
print('Searching for ', random_search)
searched = linear_searching_algorithm(random_list, random_search)
print('Search index is ', searched)



