#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import itertools
import math

"""
Created on Sun Dec 13 17:26:02 2020

@author: raymondzhang
"""

def find_sum_2020 (input_list, n):
    """
    Given a list of numbers, find n numbers
    that sum to 2020 and return their product

    Parameters
    ----------
    input_list : list
        list of integers or floats
    n : int
        number of entries to consider for sum

    Returns
    -------
    product : float or integer
        product of two numbers that add up to 2020

    error : string
        statement that no n entries sum to 2020 in the input

    """

    pairs = itertools.combinations(
        input_list, n
        )

    for pair in pairs:
        if sum(pair) == 2020:
            product = math.prod(pair)
            return product

    error = "No pair of entries that sum to 2020 exist!"

    return error

if __name__ == "__main__":
    value1 = input(
        "Please enter input as a sequence of numbers delimited by newlines :\n"
        )
    
    value2 = input(
        "Please enter input as the number of entries to consider for sum :\n"
        )

    input_list = [int(num) for num in value1.split("\n")]
    print(
        find_sum_2020(input_list, int(value2))
        )
