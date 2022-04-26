def merge_sort(arr):
    if len(arr)>1:
        mid=len(arr)//2
        L=arr[:mid]
        R=arr[mid:]
        merge_sort(L)
        merge_sort(R)
        arr.clear()
        while len(L)>0 and len(R)>0:
            if L[0]<=R[0]:
                arr.append(L[0])
                L.pop(0)
            else:
                arr.append(R[0])
                R.pop(0)
        for i in L:
            arr.append(i)
        for i in R:
            arr.append(i)
lis=list(map(int,input().split()))
print("list before sorting\n",lis)
merge_sort(lis)
print("list after sorting\n",lis)