#(just for list and dictionnaire!) faire la referance non copy. 

spam = [0, 1, 2, 3, 4, 5]
cheese = spam
cheese[1] = 'Hello'
cheese
# [0, 'Hello', 2, 3, 4, 5]
spam
# [0, 'Hello', 2, 3, 4, 5]


import copy

spam = ['A', 'B', 'C', 'D']
cheese = copy.deepcopy(spam)
cheese[1] = 42
cheese
# ['A', 42, 'C', 'D']
spam
# ['A', 'B', 'C', 'D']


#for make a new line use \ except for list (no need)

spam = ['apple', 
        'orange',
        'banana']

print('four score and seven ' + \
        'years ago')

