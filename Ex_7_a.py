#!/usr/bin/env python
import random
import threading
import plotille

result = {}


def sub_histogram(start, end, data, lock):
    sub_result = {}

    for x in data[start:end]:
        if not int(x) in sub_result:
            sub_result[int(x)] = 1
        else:
            sub_result[int(x)] += 1
    lock.acquire()
    for key in sub_result:
        if key in result:
            result[key] += sub_result[key]
        else:
            result[key] = sub_result[key]
    lock.release()

data = [random.random()*100 for i in range(1000)]
threads = 4
thread_array = []
part = int(1000 / threads)
thread_Lock = threading.Lock()
for i in range(threads):
    t = threading.Thread(target=sub_histogram,
                             args=(0 + i * part, part + i * part, data, thread_Lock))
    thread_array.append(t)
    t.start()

for thread in thread_array:
    thread.join()

print(dict(sorted(result.items(), key=lambda item: item[0])))