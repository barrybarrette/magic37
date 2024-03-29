import time
from collections import Counter
from datetime import timedelta
from random import randint

def calculate(combo_chance):
    """
    Calculate the approximate mean using this algorithm:
    Multiply the combo chance by itself.
    Check if less than our magic number 37.
    When it finally is, return the number of times we multiplied.
    Note that we do the multiply by itself as an exponent to allow for smaller increments.
    This helps get accurate readings for lower combo chances.
    """
    i = 1
    while (combo_chance / 100) ** i > 0.37:
        i += 0.005
    print(f'Mean (approx): {i:.2f}')


def measure(combo_chance, n=100000):
    """
    Measure the mean of consecutive combos over n iterations using the following algorithm:
    Pick a random number from 1 to 100
    If that number is less than the combo chance then count it as a win and keep picking random numbers.
    Otherwise, record the current combo number in the counter.
    Repeat this n times.
    Afterward, we multiply the number of times we saw each result by the result value and divide by n.

    For example:
    Imagine n is 3.
    The first run gets a combo of 2.
    The second run gets a combo of 6.
    The third run gets a combo of 2.

    In this example we saw combo 2 twice and combo 6 once, so the mean would be:
    ((2 * 2) + (6 * 1)) / 3 = 3.33 repeating
    """
    results = Counter()

    for _ in range(n):
        combo = 0
        while randint(1, 100) <= combo_chance:
            combo += 1
        results[combo] += 1

    total = 0
    for k, v in results.items():
        total += k * v
    print(f'Mean (measured): {(total / n):.2f}')


if __name__ == '__main__':
    for chance in [50, 80, 85, 90, 95, 98, 99]:
        print(f'Combo chance: {chance}%')
        calculate(chance)
        start = time.time()
        measure(chance, n=1000000)
        end = time.time()
        print(f'Time to measure: {timedelta(seconds=end - start)}')
        print('---------')