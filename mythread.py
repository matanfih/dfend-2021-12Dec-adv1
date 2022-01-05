#!/usr/bin/env python3

import threading
import time
import random


def hello(n):
    time.sleep(random.randint(0, 3))
    print(f'{n} Hello!')


for i in range(10):
    t = threading.Thread(target=hello, args=(i,))
    t.start()
