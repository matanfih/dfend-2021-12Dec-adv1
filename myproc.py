#!/usr/bin/env python3

from concurrent.futures import ProcessPoolExecutor, wait, as_completed
import glob


def file_size(filename):
    total = 0

    for one_line in open(filename):
        total += len(one_line)

    return total


if __name__ == '__main__':
    with ProcessPoolExecutor(max_workers=5) as executor:
        results = executor.map(file_size,
                               glob.glob('*.txt'))

        for one_result in results:
            print(one_result)

    print('Done!')
