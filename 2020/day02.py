#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 21:22:51 2020

@author: raymondzhang

Advent Day 2: Prompt

Part 1:
To try to debug the problem, they have created a list (your puzzle input)
of passwords (according to the corrupted database) and the corporate policy
when that password was set.

For example, suppose you have the following list:

1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc

Each line gives the password policy and then the password.
The password policy indicates the lowest and highest number of times
a given letter must appear for the password to be valid.
For example, 1-3 a means that the password must contain
a at least 1 time and at most 3 times.

Part 2:
Each policy actually describes two positions in the password,
where 1 means the first character, 2 means the second character, and so on.
(Be careful; Toboggan Corporate Policies have no concept of "index zero"!)
Exactly one of these positions must contain the given letter.
Other occurrences of the letter are irrelevant for the
purposes of policy enforcement.

Given the same example list from above:

    1-3 a: abcde is valid: position 1 contains a and position 3 does not.
    1-3 b: cdefg is invalid: neither position 1 nor position 3 contains b.
    2-9 c: ccccccccc is invalid: both position 2 and position 9 contain c.

How many passwords are valid according to the new interpretation of the policies?

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
