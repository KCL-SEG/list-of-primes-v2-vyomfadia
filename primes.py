"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    if number_of_primes <= 0:
        raise ValueError("Required number of primes must be greater than 0")

    primes = []

    i = 2
    while len(primes) < number_of_primes:
        if all([i % x != 0 for x in primes]):
            primes.append(i)

        i += 1

    return primes
