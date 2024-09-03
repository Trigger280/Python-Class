def binary_search(list,key):
    low=0 
    high=len(list)-1
    found=False
    while low<=high and not found:
        mid=(low+high)//2
        if key==list[mid]:
            found=True
        elif key>list[mid]:
            low=mid+1
        else:
            high=mid-1
    if found==True:
        print("Your number is found ",mid )
    else:
        print("Your number is not found")  

list=[1,5,26,14,77,80,9,54]
list.sort()
print(list)
key=int(input("Enter the number from the list"))
binary_search(list,key)    


