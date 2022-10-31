#!/usr/bin/python3
"""Module inherits from the list class"""


class MyList(list):
    """Class that inherits from list"""
    def print_sorted(self):
        """prints a sorted list"""
        print(sorted(self))