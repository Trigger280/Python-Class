list=[1,4,3,65,33,23,67,78,90]
print(list)
i=0
num=int(input("Enter a number from the given list : "))

while i<=len(list):
    if(num==list[i]):
        print("num found at index :", i)
        break
    i+=1

       
        
          