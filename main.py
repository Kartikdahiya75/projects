A = ([2,5,7],
     [4,2,7],
     [11,12,13])
print(A)
result = ([0,0,0],
          [0,0,0],
          [0,0,0])
for i in range (len(A)):
    for j in range (len(A[0])):
        result [j][i]=A[i][j]
for r in result:
    print(r)

    