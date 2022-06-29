import random
board=[
[[],[],[]],
[[],[],[]],
[[],[],[]]
]
lista=[1,1,1,1,1,1,1,1,1]
listb=[2,2,2,2,2,2,2,2,2]
listc=[3,3,3,3,3,3,3,3,3]
games=0
totalsteps=0
#***********************starting the game***************************************
for x in range(1,101):
    board=[
    [[],[],[]],
    [[],[],[]],
    [[],[],[]]
    ]
    steps=0
    flag=False
    total=lista+listb+listc
    for i in range(1,28):
        steps+=1
        random.shuffle(total)
        a=total.pop()
        m=random.randint(0,2)
        n=random.randint(0,2)
        if a not in board[m][n]:
            board[m][n].append(a)
        else:
            while a in board[m][n]:
                m=random.randint(0,2)
                n=random.randint(0,2)
                if a not in board[m][n]:
                    board[m][n].append(a)
                    break
        for x in board[0][0]:            #1st 00 01 02
            for y in board[0][1]:
                if x==y:
                    for z in board[0][2]:
                        if x==y==z:
                            games+=1
                            flag=True
                            break
                    if flag:
                        break
            if flag:
                break
        if flag:
            break
        for x in board[0][0]:           #2nd 00 10 20
            for y in board[1][0]:
                if x==y:
                    for z in board[2][0]:
                        if x==y==z:
                            games+=1
                            flag=True
                            break
                    if flag:
                        break
            if flag:
                break
        if flag:
            break
        for x in board[0][0]:           #3rd 00 11 22
            for y in board[1][1]:
                if x==y:
                    for z in board[2][2]:
                        if x==y==z:
                            games+=1
                            flag=True
                            break
                    if flag:
                        break
            if flag:
                break
        if flag:
            break
        for x in board[0][1]:           #4th 01 11 21
            for y in board[1][1]:
                if x==y:
                    for z in board[2][1]:
                        if x==y==z:
                            games+=1
                            flag=True
                            break
                    if flag:
                        break
            if flag:
                break
        if flag:
            break
        for x in board[0][2]:            #5th 02 12 22
            for y in board[1][2]:
                if x==y:
                    for z in board[2][2]:
                        if x==y==z:
                            games+=1
                            flag=True
                            break
                    if flag:
                        break
            if flag:
                break
        if flag:
            break
        for x in board[0][2]:           #6th 02 11 20
            for y in board[1][1]:
                if x==y:
                    for z in board[2][0]:
                        if x==y==z:
                            games+=1
                            flag=True
                            break
                    if flag:
                        break
            if flag:
                break
        if flag:
            break
        for x in board[1][0]:           #7th 10 11 12
            for y in board[1][1]:
                if x==y:
                    for z in board[1][2]:
                        if x==y==z:
                            games+=1
                            flag=True
                            break
                    if flag:
                        break
            if flag:
                break
        if flag:
            break
        for x in board[2][2]:           #8th 22 20 21
            for y in board[2][0]:
                if x==y:
                    for z in board[2][1]:
                        if x==y==z:
                            games+=1
                            flag=True
                            break
                    if flag:
                        break
            if flag:
                break
        if flag:
            break
    totalsteps=totalsteps+steps
print(9*"**")
print("total games=",games)
print("average steps= ",totalsteps/100)
