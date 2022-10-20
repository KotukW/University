def readFile():
    pyramidNums = []
    with open('6 laba\\nums.txt', 'r') as fr:
        pyramidNums = " ".join(i for i in fr.readlines()).split()
        return pyramidNums

def writeFile(pyramid):
    with open('6 laba\\pyramid.txt', 'w') as fw:
            #enters = len(pyramid)+1
            for i in pyramid:
                #fw.write(" "*enters)
                for j in i:
                    fw.write(j+" ")
                #enters -= 1
                fw.write('\n')

def main():
    pyramidNums = readFile()
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