import enchant
import argparse
from itertools import permutations


def check_spelling(word):
    us_dict = enchant.Dict('en_US')
    return us_dict.check(word)


def search_perm(perms):
    result = set()
    for perm in perms:
        if check_spelling(perm):
            result.add(perm)
    return result


def search(chars):
    for length in range(3, len(chars)+1):
        print('searching for', length, 'char words')
        for word in search_perm([''.join(p) for p in permutations(chars, length)]):
            print(word)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--chars', help='characters to check spelling against', required=True)
    args = parser.parse_args()

    if args.chars is not None:
        print('searching for {0}'.format(args.chars))

    search(args.chars)
