
import time
num=int(input("enter your choice of number"))
def table(num):
    a=1
    while a<=10:
        m= num * a
        print(num,"*",a,"=",m)
        time.sleep(1)
        a=a+1

table(num)


