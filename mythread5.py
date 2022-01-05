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

    for one_filename in glob.glob('*.txt'):
        one_future = executor.submit(hello, i)
        all_futures.append(one_future)

    for one_future in as_completed(all_futures):
        e = one_future.exception()

        if e:
            print(f'You got an exception: {e}')
        else:
            print(one_future.result())  # gives the result or exception

print('Done!')
