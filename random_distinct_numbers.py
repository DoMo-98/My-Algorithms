# import sys
from random import randint

# scaled_value = min + ( random() * ( max - min ) )
# maximum_int_value = sys.maxsize

"""
    Makes a list of distinct random numbers.
    :param qty: quantity of random numbers
    :param start: minimum value of random numbers (included)
    :param end: maximum value of random numbers (included)
"""
def random_distinct_numbers( qty, start, end ): # start = 0, end = sys.maxsize ???

    random_posibilities = list( range( start, end ) )
    random_list = []

    for _ in range( qty ):
        random_list.append( random_posibilities.pop( randint( 0, len( random_posibilities ) - 1 ) ) )

    return random_list


if __name__ == '__main__':
    qty = 10
    start = -56
    end = 123

    random_list = random_distinct_numbers( qty, start, end )
    print( random_list )