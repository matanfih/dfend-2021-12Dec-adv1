#!/usr/bin/env python3

import threading
import queue
import glob


def file_size(filename):
    total = 0

    for one_line in open(filename):
        total += len(one_line)

    q.put(total)


q = queue.Queue()
all_threads = []

for one_filename in glob.glob('*.txt'):
    t = threading.Thread(target=file_size, args=(one_filename,))
    all_threads.append(t)
    t.start()


# collect threads
for one_thread in all_threads:
    one_thread.join()

while not q.empty():
    print(q.get())
