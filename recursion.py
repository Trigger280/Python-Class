
#print("Enter your name")
#name=str(input())
#print("Length of your name is:.", len(name))
#list=(1,2,3,"Aditya","Rishav")
#print(len(list))
def cal_sum(n):
    if(n==0):
        return 0
    return cal_sum(n-1) + n
    
print(cal_sum(4))
