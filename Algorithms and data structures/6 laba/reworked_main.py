pyramidNums = []
with open('6 laba\\nums.txt', 'r') as fr:
    pyramidNums = " ".join(i for i in fr.readlines()).split()

pyramid = []
number = 0
xbost = 1

while pyramidNums != []:
    pyramid.append(pyramidNums[number:xbost])
    pyramidNums = pyramidNums[xbost::]
    xbost += 1

if len(pyramid[-1]) < len(pyramid[-2]):
    base = pyramid.pop()
    for i in base:
        pyramid[-1] += i

with open('6 laba\\pyramid.txt', 'w') as fw:
        for i in pyramid:
            for j in i:
                fw.write(j+" ")
            fw.write('\n')