import numpy as np


arr = np.array([[2,3,5],
                [7,0,1],
                [0,3,5]])
print("After Matrix ")
print(arr)
lst = [[],[]]

for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j] == 0:
            
            lst[0].append(i) # for rows
            lst[1].append(j) # for column

    for dt in range(len(lst[0])):        
        for k in range(len(arr)):
            for l in range(len(arr[k])):
                if k== lst[0][dt] or l==lst[1][dt]:
                    arr[k][l]=0


print("Before Matrix ")
print(arr)