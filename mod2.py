import time
def caltime(func):
    def inner(*args):
        st=time.monotonic()
        print("start",st)
        func()
        et=time.monotonic()
        print("end time",et)
        d=et-st
        print("toatl time =",d)
    return inner    
def fibs():
     a,b=0,1
     while(1):
         yield a
         a,b=b,a+b 
n=int(input("enter the number"))
print(n)
@caltime
def my():
    fib=fibs()
    # print(', '.join(str(next(fib)) for _ in range(n)))
    # for f in range(n-1):
    #     print(next(fib)) 
if "_main_":
    my()
 