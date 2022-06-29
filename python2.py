import random
lista=[1,1,1,1,1,1,1,1,1] #mikro kapaki
listb=[2,2,2,2,2,2,2,2,2] #messaio kapaki
listc=[3,3,3,3,3,3,3,3,3] #megalo kapaki
games=1
totalsteps=0
count=0
flag=True
# ***********************starting the game***************************************
# theoroume oti ta steps=kiniseis oti einai kathe fora pou mpainei panw ston pinaka
# kapoio kapaki aneksaritos megethous
# Ta kapakia epilegontai tixaia
# gia na oloklirwthei ena paixnidi prepei na ginei to flag=True 
while games<100:
    board=[
    [[],[],[]],
    [[],[],[]],
    [[],[],[]]
    ]
    steps=0
    flag=False
    total=lista+listb+listc #se kathe neo paixnidi i sunoliki lista perilamvanei 27 kapakia
    m=random.randint(0,2)
    n=random.randint(0,2)
    for i in range(1,28):
        random.shuffle(total)
        a=total.pop()
        while board[m][n]!=[]:
            if max(board[m][n])>a:
                m=random.randint(0,2)
                n=random.randint(0,2)
            else:
                break
        if board[m][n]==[]:
            board[m][n].append(a)
            steps+=1
        elif max(board[m][n])<a:
            board[m][n].append(a)
            steps+=1
        for x in board[0][0]:            #1st 00 01 02 (i prwti apo tis 8 theseis gia ton termatismo)
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
