#!/usr/bin/env python

import json


try:
    with open("Ex6.json", 'r') as infile:
        tasks = json.load(infile)
except:
    tasks={}
    print("No json file in directory.")

to_delete=[]

for key in tasks:
    print(key + " " +tasks[key])
    delete=input("Would you like to delete data? y/n")
    if delete=="y":
        to_delete.append(key)

for key in to_delete:
    del(tasks[key])

while True:
    new= input("Would you like add new data? y/n")
    if new=="n":
        break

    task=input("Add new task\n")
    desc = input("Add desctiption to the task\n")
    tasks[task]=desc


with open('Ex6.json', 'w') as outfile:
    json.dump(tasks, outfile)