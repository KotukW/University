import csv
from itertools import combinations

def simpleAnsw(orders, time):
    arrays, subArrays = [], []
    for i in orders:
        arrays.append(int(i[0]))
    for i in range(len(arrays)+1):
        subArrays.append([j for j in combinations(arrays,i)])
    maximum, summaMoney, summaTime = 0,0,0
    maxOrder = set()
    for i in subArrays:
        for comb in i:
            for order in comb:
                summaMoney += int(orders[str(order)][1])
                summaTime += int(orders[str(order)][0])
            if summaMoney > maximum and summaTime <= int(time):
                maximum = summaMoney
                maxOrder = comb
            summaMoney, summaTime = 0, 0
    return maxOrder

orders = {}
with open("8 laba\\delivery.csv") as f:
    orders = {}
    reader = csv.reader(f)
    for row in reader:
        orders[row[0]]= [row[1], row[2]]
orders.pop("order")

timeLimit = input("Input time limit: ")
arrays, subArrays = [], []
for i in orders:
    arrays.append(int(i[0]))
for i in range(len(arrays)+1):
    subArrays.append([j for j in combinations(arrays,i)])
maximum, summaMoney, summaTime = 0,0,0
maxOrder = set()
for i in subArrays:
    for comb in i:
        for order in comb:
            summaMoney += int(orders[str(order)][1])
            summaTime += int(orders[str(order)][0])
        if summaMoney > maximum and summaTime <= int(timeLimit):
            maximum = summaMoney
            maxOrder = comb
        summaMoney, summaTime = 0, 0
print(maxOrder)
