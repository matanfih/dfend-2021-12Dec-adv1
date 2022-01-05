#!/usr/bin/env python3

import threading
import queue
import glob
import time


def file_size(filename):
    total = 0

    for one_line in open(filename):
        total += len(one_line)

    q.put((filename, total))


q = queue.Queue()
all_threads = []

start_time = time.perf_counter()
for one_filename in glob.glob('*.txt'):
    t = threading.Thread(target=file_size, args=(one_filename,))
    all_threads.append(t)
    t.start()


# collect threads
for one_thread in all_threads:
    one_thread.join()


end_time = time.perf_counter()
total = 0
while not q.empty():
    filename, file_total = q.get()
    print(f'Got {filename}, size {total}')
    total += file_total
print(f'{total=}')
print(f'Total time: {end_time-start_time}')
