#Solution of Knight's Tour. Backtracking and recursive.
N = int(input("Input number of moves you want the knight to make: ")) # 64 for complete tour
from sys import exit
def move(i, j, ans): # available position
    cont = []
    if (i-1 >= 0 and j-2 >= 0 and (i-1, j-2) not in ans):  
        cont.append((i-1, j-2))
    if (i+1 <= 7 and j-2 >= 0 and (i+1, j-2) not in ans):
        cont.append((i+1, j-2))
    if (i-2 >= 0 and j-1 >= 0 and (i-2, j-1) not in ans):
        cont.append((i-2, j-1))
    if (i+2 <= 7 and j-1 >= 0 and (i+2, j-1) not in ans):
        cont.append((i+2, j-1))
    if (i-2 >= 0 and j+1 <= 7 and (i-2, j+1) not in ans):
        cont.append((i-2, j+1))
    if (i+2 <= 7 and j+1 <= 7 and (i+2, j+1) not in ans):
        cont.append((i+2, j+1))
    if (i-1 >= 0 and j+2 <= 7 and (i-1, j+2) not in ans):
        cont.append((i-1, j+2))
    if (i+1 <= 7 and j+2 <= 7 and (i+1, j+2) not in ans):
        cont.append((i+1, j+2))
    return cont
def show(ans): # print answer
    form = [[0 for _ in range(8)] for _ in range(8)]
    for i in range(len(ans)):
        form[ans[i][0]][ans[i][1]] = i+1
    for i in range(8):
        for j in range(8):
            print(str(form[i][j]) if form[i][j] > 9 else "0" + str(form[i][j]), end='|')
        print()   
def tour(ans, count): # compute next move, and recurse
    if count == N-1:
        print("Solution:")
        show(ans)
        exit()
    space = move(ans[count][0], ans[count][1], ans)
    count = count+1
    if space == []:
        count = count-1
        ans.pop()
    else:
        for x in space:
            ans.append(x)
            tour(ans, count)
        count = count-1
        ans.pop()
for i in range(8):
    for j in range(8):
        tour([(0, 0)], 0) # try every starting position
