def quick_sort(arr):
    length=len(arr)
    if length<=1:
        return arr
    else:
        peviot=arr.pop()
    greater_ele=[]
    smaller_ele=[]
    for item in arr:
        if item>peviot:
            greater_ele.append(item)
        else:
            smaller_ele.append(item)
    peviot=[peviot]
    return quick_sort(smaller_ele)+peviot+quick_sort(greater_ele)

lis=list(map(int,input().split()))
print("list before sorting\n",lis)
print("list after sorting\n",quick_sort(lis))