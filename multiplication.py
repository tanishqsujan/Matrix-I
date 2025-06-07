x= [[3,7],
    [8,9]]

y= [[8,9],
    [2,5]]

answer= [[0,0],
         [0,0]]

#iterate through rows of x
for i in range(len(x)):
    for j in range(len(y[0])):
        for k in range(len(y)):
            answer[i][j] += x[i][k] * y[k][j]
            
for r in answer:
    print(r)