from copy import deepcopy

class Animal:
    pass

def process(animals):
    for t in range(0, 100):
        copy = deepcopy(animals)
        for i in range(len(animals)):
            variation = animals[i].rep * copy[i].pop
            if(animals[i-1].ids == animals[i].id):
                variation -= animals[i-1].man * copy[i-1].pop
            animals[i].pop += variation
        i = 0
        while(i < len(animals)):
            if(animals[i].pop <= 0):
                del(animals[i])
            else:
                i += 1
        if (len(animals) == 1):
            break
    newTab = []
    for i in range(0, len(animals)):
        newTab.append(animals[i].id)
    return newTab

def displayArray(tab):
    s = ""
    for t in tab:
        s += str(t) + " "
    s = s[:-1]
    print(s)

def main():
    f = open("PRV.in", mode = "r")

    lines = f.read().split("\n")
    nbProblems = int(lines[0])
    index = 1
    for i in range(0, nbProblems):
        animals = []
        id = 0
        for j in range(index + 1, index + 1 + int(lines[index])):
            l = lines[j].split(" ")
            a = Animal()
            a.id = id
            if(j == index + int(lines[index])):
                a.ids = 0
            else:
                a.ids = id + 1
            a.pop = int(l[0])
            a.rep = int(l[1])
            a.man = int(l[2])
            animals.append(a)
            id += 1
        index += int(lines[index]) + 1
        displayArray(process(animals))

    f.close()

main()
