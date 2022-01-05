#!/usr/bin/env python3

from concurrent.futures import ThreadPoolExecutor, wait, as_completed
import time
import random


def hello(n):
    time.sleep(random.randint(0, 3))
    print(f'{n} Hello')
    print(f'{n} Goodbye')

    if n == 5:
        raise ValueError('I do not like 5!')

    return f'{n} Done'


with ThreadPoolExecutor(max_workers=5) as executor:
    all_futures = []

    for i in range(10):
        one_future = executor.submit(hello, i)
        all_futures.append(one_future)

    for one_future in as_completed(all_futures):
        e = one_future.exception()

        if e:
            print(f'You got an exception: {e}')
        else:
            print(one_future.result())  # gives the result or exception

print('Done!')
