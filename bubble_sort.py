arr=list(map(int,input().split()))
print("list before sorting\n",arr)
for i in range(len(arr)):
    for j in range(len(arr)-1):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
print("list after sorting\n",arr)