import random
def create_matrix(size):
    arr=[]
    for i in range(size):
        col=[]
        for j in range(size):
            col.append(random.randint(0,1))
        arr.append(col)
    return arr

def init_count(size):
    count=[]
    for i in range(size):
        col=[]
        for j in range(size):
            col.append(0)
        count.append(col)
    return count

def print_matrix(arr):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            print(arr[i][j],end=" ")
        print()
        
def alive(arr,i,j,x,y):
    if ((x!=i or y!=j) and arr[x][y]==1):
        return True
    else:
        False

def count_inside(arr,i,j):
    _count=0
    for x in range(i-1,i+2):
        for y in range(j-1,j+2):
            if alive(arr,i,j,x,y):
                _count+=1
    return _count

def count_upper_left_corner(arr):
    _count=0
    for x in range(2):
        for y in range(2):
            if alive(arr,0,0,x,y):
                _count+=1
    return _count

def count_upper_right_corner(arr):
    _count=0
    for x in range(2):
        for y in range(len(arr)-2,len(arr)):
            if alive(arr,0,len(arr)-1,x,y):
                _count+=1
    return _count

def count_upper_middle_corner(arr,j):
    _count=0
    for x in range(2):
        for y in range(j-1,j+2):
            if alive(arr,0,j,x,y):
                _count+=1
    return _count

def count_upper_line(arr,i,j):
    if j==0:
        return count_upper_left_corner(arr)
    elif j==len(arr)-1:
        return count_upper_right_corner(arr)
    else:
        return count_upper_middle_corner(arr,j)

def count_lower_left_corner(arr):
    _count=0
    for x in range(len(arr)-2,len(arr)):
        for y in range(len(arr)-2,len(arr)):
            if alive(arr,len(arr)-1,0,x,y):
                _count+=1
    return _count

def count_lower_right_corner(arr):
    _count=0
    for x in range(len(arr)-2,len(arr)):
        for y in range(len(arr)-2,len(arr)):
            if alive(arr,len(arr)-1,len(arr)-1,x,y):
                _count+=1
    return _count

def count_lower_middle_corner(arr,j):
    _count=0
    for x in range(len(arr)-2,len(arr)):
        for y in range(j-1,j+2):
            if alive(arr,len(arr)-1,j,x,y):
                _count+=1
    return _count

def count_lower_line(arr,i,j):
    if j==0:
        return count_lower_left_corner(arr)
    elif j==len(arr)-1:
        return count_lower_right_corner(arr)
    else:
        return count_lower_middle_corner(arr,j)

def count_left_line(arr,i,j):
    _count=0
    for x in range(i-1,i+2):
        for y in range(2):
            if alive(arr,i,j,x,y):
                _count+=1
    return _count

def count_right_line(arr,i,j):
    _count=0
    for x in range(i-1,i+2):
        for y in range(len(arr)-2,len(arr)):
            if alive(arr,0,len(arr)-1,x,y):
                _count+=1
    return _count

def count_alive(arr,count):
    count=init_count(len(count))
    for i in range(len(arr)):
        for j in range(len(arr)):
            #count[i][j]=0
            if((i!=0 and i!=len(arr)-1) and (j!=0 and j!=len(arr)-1)):
                count[i][j]=count_inside(arr,i,j)
            else:
                if i==0:
                    count[i][j]=count_upper_line(arr,i,j)
                elif i==len(arr)-1:
                    count[i][j]=count_lower_line(arr,i,j)
                elif j==0:
                    count[i][j]=count_left_line(arr,i,j)
                elif j==len(arr)-1:
                    count[i][j]=count_right_line(arr,i,j)
    return count

def live(arr,count):
    if((count == 2 or count == 3) and arr == 1):
        return True
    else:
        False

def born(arr,count):
    if(count==3 and arr==0):
        return True
    else:
        return False

def update_matrix(arr,count):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if live(arr[i][j],count[i][j]):
                    arr[i][j]=1
            elif born(arr[i][j],count[i][j]):
                    arr[i][j]=1
            else:
                arr[i][j]=0
    return arr

import os,time
arr=[[0,0,0,0,0],[0,0,0,0,0],[0,1,1,1,0],[0,0,0,0,0],[0,0,0,0,0]]
# arr=create_matrix(int(input("enter size: ")))
count = init_count(len(arr))
os.system('clear')
# print_matrix(arr)
# print()
# print_matrix(count)
print()
while(True):
    print_matrix(update_matrix(arr,count_alive(arr,count)))
    time.sleep(.5)
    os.system('clear')
    print()
