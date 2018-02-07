#!/bin/python3


'''
This gives the digit count
'''


def find_digits(num_fun):
    '''
    Counts the digits
    '''
    converted = str(num_fun)
    count = 0
    for loop_var in converted:
        if(int(loop_var) != 0 and num_fun % int(loop_var) == 0):
            count = count + 1
    print(count)
    # Complete this function


if __name__ == "__main__":
    COUNT = int(input().strip())
    for a0 in range(COUNT):
        num = int(input().strip())
        find_digits(num)
