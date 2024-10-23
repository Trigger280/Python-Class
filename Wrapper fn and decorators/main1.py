#Write a function that evaluates a expression res = 1 * 10 for all values between 0 to n
import time
n=10000000

def testfn(n):
    for i in range (0,n):
        res=i*10

start_time=time.time() * 1000 #multiplying by 1000 to covert time into milliseconds
#execute fucntion
testfn(n)

end_time=time.time() * 1000
diff = end_time - start_time

print(f"Execution time for n = {n} is \n {diff} sec")