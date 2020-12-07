#!/usr/bin/env python

import random

first_number=True
to_sort=[]
for a in range(50):
    to_sort.append(random.randint(0,100))
sorted=[]
for item in to_sort:
    if first_number:
        sorted.append(item)
        first_number=False
        continue
    added=False
    for new_item in sorted:
        if item < new_item:
            continue
        else:
            sorted.insert(sorted.index(new_item),item)
            added=True
            break
    if not added:
        sorted.append(item)

print((sorted))