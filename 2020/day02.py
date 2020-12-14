#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 21:22:51 2020

@author: raymondzhang
"""

def check_code_part_1(code_list):
    """
    Parameters
    ----------
    code_list :  list of strings
        list of corporate password policies corresponding to passwords
        format: (lower bound)-(upper bound) letter: password

    Returns
    -------
    num_code_correct : int
        number of passwords that adhere to corporate policy

    """

    num_code_correct = 0

    for code in code_list:

        policy, letter, password = code.split(" ")
        criteria = [int(i) for i in policy.split("-")]

        # get rid of extra colon
        letter = letter[0]

        letters_counted = password.count(letter)

        if letters_counted >= criteria[0] and letters_counted <= criteria[1]:
            num_code_correct += 1

    return num_code_correct

def check_code_part_2(code_list):
    """
    Parameters
    ----------
    code_list :  list of strings
        list of corporate password policies corresponding to passwords
        format: (lower bound)-(upper bound) letter: password

    Returns
    -------
    num_code_correct : int
        number of passwords that adhere to corporate policy

    """

    num_code_correct = 0

    for code in code_list:

        policy, letter, password = code.split(" ")
        criteria = [int(i) for i in policy.split("-")]

        # get rid of extra colon
        letter = letter[0]

        condition1 = password[criteria[0]-1] == letter
        condition2 = password[criteria[1]-1] == letter

        if condition1 != condition2:
            num_code_correct += 1

    return num_code_correct

if __name__ == "__main__":

    value = input(
        "Input the list of corporate policies and passwords, delimited by newlines"
        )
    input_list = [i for i in value.split("\n")]

    print(check_code_part_1(input_list))
    print(check_code_part_2(input_list))
