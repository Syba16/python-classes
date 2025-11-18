# Speed=Distance / Time. Write a function such if any of two of the Variables are given, the function should be able to give the third variable (Physics - Mechanics) 
# Eg: If Speed and Time is given, Distance can be determined.

def calculate_dist():

    speed=float(input("enter speed value:"))
    time=float(input("enter time value:"))
    dist=float(input("enter distance value:"))

    if speed>0 and time>0:
            dist=speed*time
            print("Distance =",dist,"km/hrs")

    elif dist>0 and time<=60:
            speed=dist/time
            print("speed=",speed,"km/hrs")

    elif speed>0 and dist>0:
            time=dist/speed
            print("time=",time,"hrs")

    else:
            print("Insufficient Data")
        
calculate_dist()