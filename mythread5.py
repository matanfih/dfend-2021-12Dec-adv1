#!/usr/bin/env python3

from concurrent.futures import ThreadPoolExecutor, wait, as_completed
import glob


def file_size(filename):
    total = 0

    for one_line in open(filename):
        total += len(one_line)

    return total


with ThreadPoolExecutor(max_workers=5) as executor:
    all_futures = []
    results = executor.map(file_size,
                           glob.glob('*.txt'))

    print(list(results))

print('Done!')
