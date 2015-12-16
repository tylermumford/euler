#!/usr/bin/env python3

collatz_memo = {1: 1}

def collatz(n):
    '''Return the length of the Collatz sequence for the given input'''

    if n in collatz_memo:
        result = collatz_memo[n]
    elif n % 2 == 0:
        collatz_memo[n] = 1 + collatz(n / 2)
        result = collatz_memo[n]
    else:
        collatz_memo[n] = 1 + collatz(3 * n + 1)
        result = collatz_memo[n]

    return result


if __name__ == '__main__':
    import argparse
    desc = 'Return the collatz number for a given input'
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('n', type=int, help='integer to use as input')

    args = parser.parse_args()
    print(collatz(args.n))
