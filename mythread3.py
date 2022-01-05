#!/usr/bin/env python3

from concurrent.futures import ThreadPoolExecutor
import time
import random


def hello(n):
    time.sleep(random.randint(0, 3))
    print(f'{n} Hello')
    print(f'{n} Goodbye')


with ThreadPoolExecutor(max_workers=5) as executor:
    for i in range(10):
        executor.submit(hello, i)

# wait for threads
for one_thread in all_threads:
    one_thread.join()   # wait for this thread to end


print('Done!')
