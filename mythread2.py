#!/usr/bin/env python3

import threading
import time
import random
import queue


q = queue.Queue()


def hello(n):
    time.sleep(random.randint(0, 3))
    q.put(f'{n} Hello!')


# start threads
all_threads = []
for i in range(10):
    t = threading.Thread(target=hello, args=(i,))
    all_threads.append(t)
    t.start()

# wait for threads
for one_thread in all_threads:
    one_thread.join()   # wait for this thread to end


print('Done!')

while not q.empty():
    print(q.get())
