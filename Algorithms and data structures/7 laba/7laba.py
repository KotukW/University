def readFile():
    pyramidNums = []
    with open('6 laba\\pyramid.txt', 'r') as fr:
        for i in fr:
            pyramidNums += i.strip("\n").split()
        return pyramidNums

def writeFile(pyramid):
    with open('7 laba\\pyramid.txt', 'w') as fw:
            #enters = len(pyramid)+1
            for i in pyramid:
                #fw.write(" "*enters)
                for j in i:
                    fw.write(j+" ")
                #enters -= 1
                fw.write('\n')

def main():
    pyramidNums = readFile()
    delete = input()
    for num in pyramidNums:
        if num == delete:
            pyramidNums.remove(num)
    n, k = 0, 1
    pyramid = []
    while pyramidNums != []:
        pyramid.append(pyramidNums[n:k])
        pyramidNums = pyramidNums[k::]
        k += 1
    if len(pyramid[-1]) < len(pyramid[-2]):
        base = pyramid.pop()
        for i in base:
            pyramid[-1] += i
    writeFile(pyramid)


if __name__ == '__main__':
    main()