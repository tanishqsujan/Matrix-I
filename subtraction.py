x= [[10,8],
    [4,5]]

y= [[9,3],
    [6,7]]

answer= [[0,0],
         [0,0]]

for i in range(len(x)):
    for j in range(len(x[0])):
        answer[i][j]= x[i][j] - y[i][j]
        
for r in answer:
    print(r)