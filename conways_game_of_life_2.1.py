# import random
# size = int(input("enter the size of arr: "))
# arr=[]
# for i in range(size):
#     col=[]
#     for j in range(size):
#         n=random.randint(0,1)
#         col.append(n)
#     arr.append(col)
arr=[[0,0,0,0,0],[0,0,0,0,0],[0,1,1,1,0],[0,0,0,0,0],[0,0,0,0,0]]
# arr=[[1,0,1,0,1],[0,1,0,1,0],[1,0,1,0,1],[0,1,0,1,0],[1,0,1,0,1]]
size=5
count=[]
for i in range(size):
    col2=[]
    for j in range(size):
        col2.append(0)
    count.append(col2)

for i in range(size):
    for j in range(size): 
        print(arr[i][j],end=" ")
    print()
print()
print()
print()
for z in range(10):
    for i in range(size):
        for j in range(size):
            count[i][j]=0
            if((i!=0 and i!=size-1) and (j!=0 and j!=size-1)):
                for x in range(i-1,i+2):
                    for y in range(j-1,j+2,1):
                        if(i!=x or j!=y):
                            if(arr[x][y]==1):
                                count[i][j]+=1
            else:
                if i==0 and j==0:
                    for x in range(i+2):
                        for y in range(j+2):
                            if x!=i or y!=j:
                                if arr[x][y]==1:
                                    count[i][j]+=1
                elif i==0 and (j < size-1 and j>0):
                    for x in range(i+2):
                        for y in range(j-1,j+2):
                            if x!=i or y!=j:
                                if arr[x][y]==1:
                                    count[i][j]+=1
                elif i==0 and j== size-1:
                    for x in range(i+2):
                        for y in range(j-1,j+1):
                            if x!=i or y!=j:
                                if arr[x][y]==1:
                                    count[i][j]+=1
                elif (i < size-1 and i > 0) and j==0:
                    for x in range(i-1,i+2):
                        for y in range(j+2):
                            if x!=i or y!=j:
                                if arr[x][y]==1:
                                    count[i][j]+=1
                elif i == size-1 and j==0:
                    for x in range(i-1,i+1):
                        for y in range(j+2):
                            if x!=i or y!=j:
                                if arr[x][y]==1:
                                    count[i][j]+=1
                elif (i>0 and i < size-1) and j == size-1:
                    for x in range(i-1,i+2):
                        for y in range(size-2,size):
                            if x!=i or y!=j:
                                if arr[x][y]==1:
                                    count[i][j]+=1
                elif i == size-1 and (j>0 and j < size-1):
                    for x in range(i-1,i+1):
                        for y in range(j-1,j+2):
                            if x!=i or y!=j:
                                if arr[x][y]==1:
                                    count[i][j]+=1
                elif i == size-1 and j == size-1:
                    for x in range(i-1,i+1):
                        for y in  range(j-1,j+1):
                            if x!=i and y!=j:
                                if arr[x][y]==1:
                                    count[i][j]+=1
    for i in range(size):
            for j in range(size):
                if((count[i][j] ==2 or count[i][j]==3) and arr[i][j]==1):
                    arr[i][j]=1
                elif(count[i][j]==3 and arr[i][j]==0):
                    arr[i][j]=1
                else:
                    arr[i][j]=0
    print("updated")
    for i in range(size):
        for j in range(size): 
            print(arr[i][j],end=" ")
        print()
    print()
    print()
    print()
    print()