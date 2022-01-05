#!/usr/bin/env python3

import threading
import queue


def file_size(filename):
    total = 0

    for one_line in open(filename):
        total += len(one_line)

    return total


q = queue.Queue()
all_threads = []
