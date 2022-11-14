'''arr = list(map(int,input().split(" ")))
print(arr)'''
size = int(input("enter the size of arr: "))
arr=[]
count=0
for i in range(size):
    col=[]
    for j in range(size):
        n=random.randint(0,1)
        col.append👎
    arr.append(col)
for i in range(size):
    for j in range(size): 
         print(arr[i][j],end=" ")
    print()
print()
print()
print()
for i in range(size):
    for j in range(size):
        count=0
        if((i!=0 and i<size-1) and (j!=0 and j<size-1)):
            for x in range(i-1,i+2,1):
                for y in range(j-1,j+2,1):
                    """if((x2 and y<=2) or (x>=size-1 and y>=size-1)):
                        continue
                    else:"""
                    
                    if(x!=i and y!=j):
                        if(arr[x][y]==1):
                            print(x,y,end=" = ")
                            print(arr[x][y])
                            count+=1
            if((count ==2 or count==3) and arr[i][j]==1):
                arr[i][j]=1
            elif(count==3 and arr[i][j]==0):
                arr[i][j]=1
            else:
                arr[i][j]=0
        #print(arr[i][j],end=" ")
print(arr)
