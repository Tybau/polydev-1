def add(string, char, left):
    global pos
    if (left == 0):
        pos.add(string)
        return
    for i in range(0, len(string) + 1):
        add(string[0:i]+char+string[i:len(string)], char, left - 1)

data = open("dungeon.in").read()
lign = data.split("\n")
nb_case = (int)(lign[0])
read = 1
res = ""
for case in range(0, nb_case):
    stats = lign[read].split(" ")
    read += 1
    height = (int)(stats[0])
    width = (int)(stats[1])
    board = []
    for i in range(0, height):
        board.append(lign[read].split(" "))
        read += 1

    pos = set([])
    string = ""
    for i in range(0, width - 1):
        string += "R"

    add(string, 'D', height - 1)

    res = 100000
    for i in pos:
        x = 0
        y = 0
        life = (int)(board[x][y])
        minLife = life
        for j in i:
            if (j == 'R'):
                y += 1
            if (j == 'D'):
                x += 1
            life += (int)(board[x][y])
            if(life < minLife):
                minLife = life
        if (minLife > 0):
            minLife = 1
        else:
            minLife = 0 - minLife + 1
        if (minLife < res):
            path = i
            res = minLife

    print(res)
