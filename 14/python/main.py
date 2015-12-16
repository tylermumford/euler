#!/usr/bin/env python3

if __name__ == '__main__':
    from collatz import collatz
    import argparse

    desc = 'Find the number with the longest Collatz sequence under a given ceiling.'
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('ceiling', type=int, default=13, nargs='?')
    args = parser.parse_args()

    ceiling = args.ceiling
    results = {}


    for x in range(ceiling - 1, 1, -2):
        results[collatz(x)] = x

    longest = max(iter(results))
    answer = results[longest]
    print("Longest: C{0} for {1}".format(longest, answer))

    print_all = False
    if print_all:
        for i in range(0, len(results)):
            print("{0}: {1}".format(i+1, results[i]), end="\t")
        print("");

