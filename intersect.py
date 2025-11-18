# Given 2 circles, can you determine if 2 circles are intersecting?
import time
# co-ordinates for first circle
r1=int(input("enter radius of first circle :"))
x1=int(input("enter value for x1:"))
y1=int(input("enter value for y1:"))

# co-ordinates for second circle
r2=int(input("enter radius of second circle :"))
x2=int(input("enter value for x2:"))
y2=int(input("enter value for y2:"))

dist=(((x2-x1)**2)+((y2-y1)**2))**1/2
print(dist)

if dist>(r1-r2):
    print("wait a moment....!!! ")
    time.sleep(2)
    print(" NO !! circle's  are not intersecting")

elif dist<(r1-r2):
    print("wait a moment....!!! ")
    time.sleep(2)
    print(" BINGO !! circle's  are intersecting")

elif dist==(r1-r2):
    print("wait a moment....!!! ")
    time.sleep(2)
    print(" WELL !! circle's  coincide with common center")
    
else:
    print("invalid data")
