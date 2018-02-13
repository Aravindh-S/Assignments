"""
    This uses numpy and does the operation
"""
import numpy as np


def sum_prod(xin, yin):

    """
      This uses numpy and does the operation
    """
    xvar, yvar = np.meshgrid(xin, yin, sparse=True)
    return np.sum(np.array(xvar * yvar))


def main():
    """
    This is the main function where arguments are passed
    """
    print(sum_prod(np.arange(3000), np.arange(3000)))


main()
