#!/usr/bin/env python3

from concurrent.futures import ThreadPoolExecutor, wait, as_completed
import glob


def file_size(filename):
    total = 0

    for one_line in open(filename):
        total += len(one_line)

    if total % 2:
        raise ValueError('Odd number of characters')

    return total


with ThreadPoolExecutor(max_workers=5) as executor:
    results = executor.map(file_size,
                           glob.glob('*.txt'))

    print(results)
    for one_result in results:
        print(one_result)

print('Done!')
