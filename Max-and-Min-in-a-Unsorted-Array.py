def get_min_max(ints):

    mini = maxi = ints[0]

    for i in ints:
        if i <= mini:
            mini = i
        if i >= maxi:
            maxi = i
    return mini, maxi


import random

test1 = [i for i in range(0, 10)]
random.shuffle(test1)
print("Pass" if ((0, 9) == get_min_max(test1)) else "Fail")

test2 = [1]
print("Pass" if ((1, 1) == get_min_max(test2)) else "Fail")

test3 = [0, 0]
print("Pass" if ((0, 0) == get_min_max(test3)) else "Fail")