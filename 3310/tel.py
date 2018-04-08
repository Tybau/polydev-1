def crypt(kb, msg):
    kb = kb.split(" ")
    crypted_msg = ""

    for c in msg:
        if(c == ' '):
            crypted_msg += "0."
            continue
        for i in range(len(kb)):
            p = kb[i].find(c)
            for j in range(p + 1):
                crypted_msg += str(i + 1) + " "
        crypted_msg = crypted_msg[:-1]
        crypted_msg += "."
    crypted_msg = crypted_msg[:-1]
    return crypted_msg

def main():
    f = open("tel.in", mode = "r")

    lines = f.read().split("\n")
    nbProblems = int(lines[0])
    index = 1
    for i in range(1, nbProblems * 2 + 1, 2):
        print(crypt(lines[i], lines[i + 1]))
    
    f.close()

main()
