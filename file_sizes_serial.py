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
    file_size(one_filename)

end_time = time.perf_counter()
