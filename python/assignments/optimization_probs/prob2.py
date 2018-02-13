"""
    This uses numpy and does the operation of counting all possible pairs such that x[i]<y[j]
"""
import numpy as np


def count_if(xin, yin):
    """
      This uses numpy boolean array and returns the sum
    """
    xvar, yvar = np.meshgrid(xin, yin, sparse=True)
    final = np.sum((np.array(xvar < yvar)))
    print(final)


def main():
    """
    This is the main function where arguments are passed
    """
    print(count_if(np.arange(0, 200, 2), np.arange(40, 140)))


main()
