"""
Program: validation_with_try.py
Author: Levi Shepherd
Last date modified: 9/21/2020

The purpose of this program is to implement the use of try/catch and
the use of raising exceptions to combat bad input from users.
"""


def average(score1, score2, score3):
    NUMBER_TESTS = 3

    if score1 < 0:
        raise ValueError("Negative numbers are not allowed")
    elif score2 < 0:
        raise ValueError("Negative numbers are not allowed.")
    elif score3 < 0:
        raise ValueError("Negative numbers are not allowed.")
    else:
        return float((score1 + score2 + score3) / NUMBER_TESTS)
