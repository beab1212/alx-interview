#!/usr/bin/python3
""" MINOPRATION Calculate minimum operations """


def minOperations(n):
    """ Calculate minimum operations to copy-all and past to get
        length of n
        Args:
            n (int): length of chracter
        Returns:
            Numbers of oprations
    """
    number_oprations = 0
    minimum_opration = 2
    while n > 1:
        while n % minimum_opration == 0:
            number_oprations += minimum_opration
            n /= minimum_opration
        minimum_opration += 1
    return number_oprations
