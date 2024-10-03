#!/usr/bin/python3
"""
Define isWineer function, a solution to the Prime Game problem
"""


def primes(n):
    """Return list of prime numbers between 1 and n inclusive
       Args:
        n (int): upper boundary of range. lower boundary is always 1
    """
    prime = []
    sieve = [True] * (n + 1)
    for p in range(2, n + 1):
        if (sieve[p]):
            prime.append(p)
            for i in range(p, n + 1, p):
                sieve[i] = False
    return prime


def isWinner(x, nums):    
    """
    Determines the winner of the Prime Game.

    Args:
        x (int): The number of rounds to be played in the game.
        nums (list[int]): A list of upper limits for each round.
                        Each element in the list
            represents the maximum number that can be chosen
            in the corresponding round.

    Returns:
        The name of the winner ("Maria" or "Ben"), or None
        if there is no clear winner.
    """
    if not x or not nums:
        return None

    maria_wins = ben_wins = 0

    for round_limit in nums:
        primes_in_round = primes(round_limit)
        if len(primes_in_round) % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
