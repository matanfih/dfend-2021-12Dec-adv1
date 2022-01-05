#!/usr/bin/env python3

import threading


def file_size(filename):
    total = 0

    for one_line in open(filename):
        total += len(one_line)

    return total


all_threads = []
