A = [[2,5,7],
     [4,2,7],
     [11,12,13]]
B = [[5,8,1], 
    [6,7,3],
    [4,5,9]]
result = [[0,0,0],
         [0,0,0],
         [0,0,0]]
for i in range(len(A)):
    for j in range (len(B[0])):
        for k in range(len(B)):
            result[i][j] += A[i][k] * B[k][j]
for r in result: 
    print(r) 




    