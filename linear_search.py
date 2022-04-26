arr=[7,9,5,3,0,17,14,17]
flag=0
ele=int(input("enter element to find: "))
for i in range(len(arr)):
    if arr[i]==ele:
        print(f"element {ele} present at index {i}")
        flag=1
if flag==0:
    print(f"element {ele} not found")