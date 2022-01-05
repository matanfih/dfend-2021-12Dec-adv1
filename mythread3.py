#!/usr/bin/env python3

from concurrent.futures import ThreadPoolExecutor
import time
import random


def hello(n):
    time.sleep(random.randint(0, 3))
    print(f'{n} Hello')
    print(f'{n} Goodbye')
    return f'{n} Done'


with ThreadPoolExecutor(max_workers=5) as executor:
    for i in range(10):
        executor.submit(hello, i)

print('Done!')
