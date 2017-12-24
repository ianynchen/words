import enchant
import argparse
from itertools import permutations
from multiprocessing import Pool
import os


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


def search_permutation(permutation, length):
    print('searching for', length, 'char words')
    print('pid:', os.getpid(), 'parent pid:', os.getppid())
    for word in search_perm(permutation):
        print(word)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--chars', help='characters to check spelling against', required=True)
    args = parser.parse_args()

    if args.chars is not None:
        print('searching for {0}'.format(args.chars))

    length = len(args.chars) + 1
    p = Pool(length - 3)
    for i in range(3, length):
        p.apply_async(search_permutation, args=([''.join(p) for p in permutations(args.chars, i)], i))
    p.close()
    p.join()

