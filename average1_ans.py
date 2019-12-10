#!/usr/bin/python3

#Book exercise Programming in Python 3 - Mark Summerfield

listNumber = []

try:
    while True:
        listNumber.append(int(input("enter a number or Enter to finish: ")))
except ValueError:
    print("numbers:", listNumber)
    print("count = {}".format(len(listNumber)))
    print("sum = {}".format(sum(listNumber)))
    print("lowest = {}".format(min(listNumber)))
    print("highest = {}".format(max(listNumber)))
    print("mean = {}".format(sum(listNumber) / len(listNumber)))
