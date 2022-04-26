def instertion_sort(arr):
    for i in range(len(lis)-1):
        j=i
        while arr[j]>arr[j+1] and j>=0:
            arr[j+1],arr[j]=arr[j],arr[j+1]
            j-=1
lis=list(map(int,input().split()))
print("list before sorting\n",lis)
instertion_sort(lis)
print("list after sorting\n",lis)
