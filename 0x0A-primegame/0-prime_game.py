#!/usr/bin/python3
"""
Define isWineer function, a solution to the Prime Game problem
"""


def primes(n):
    """Return list of prime numbers between 1 and n inclusive
       Args:
        n (int): upper boundary of range. lower boundary is always 1
    """
    if n < 2:
        return []

    primes = [2]
    sieve = [True] * (n + 1)

    for p in range(3, n + 1, 2):
        if sieve[p]:
            primes.append(p)
            for i in range(p * p, n + 1, p * 2):
                sieve[i] = False

    return primes


def isWinner(x, nums):
    """
    Determines the winner of the Prime Game.
    Args:
        x (int): The number of rounds to be played in the game.
        nums (list[int]): A list of upper limits for each round.
        Each element in the list represents the maximum number
        that can be chosen in the corresponding round.

    Returns:
        The name of the winner ("Maria" or "Ben"), or None if
        there is no clear winner.
    """
    if x is None or nums is None or x == 0 or nums == []:
        return None
    Maria = Ben = 0
    for i in range(x):
        prime = primes(nums[i])
        if len(prime) % 2 == 0:
            Ben += 1
        else:
            Maria += 1
    if Maria > Ben:
        return 'Maria'
    elif Ben > Maria:
        return 'Ben'
    return None
