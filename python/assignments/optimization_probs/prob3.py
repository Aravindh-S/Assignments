"""
    This uses numpy and does the operation of counting all possible pairs such that x[i]<y[j]
"""
import numpy as np


def remove_missing(xin, missing=-1, value=0):
    """
      This uses numpy boolean array and returns the sum
    """
    xin[xin == missing] = value
    return xin


def main():
    """
    This is the main function where arguments are passed
    """
    print(remove_missing(np.arange(0, 20, 2), 2, 1171997))


main()
