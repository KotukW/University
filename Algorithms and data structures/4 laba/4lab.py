import os
print(os.listdir(os.getcwd()))

fr = open('4 laba\\graph.txt', 'r') # Поменяй путь до файла
every_line = [string.strip("\n").split(":") for string in fr]
graph = {}
node = input()
for line in every_line:
    graph[line[0]] = line[1]    
if node in graph:
    for i in graph[node]:
        print(i, end=" ")
else:
    print("Theres no such node")
fr.close()