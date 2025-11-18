# program without functions

# model to test if a Point is inside a Circle (Geo Spatial - ML - Geometry)

# take  x1,y1 values represent the point co-ordinates
x1=int(input("enter x1:"))
y1=int(input("enter y1:"))

# take  c1,c2 values represent the center co-ordinates
c1=int(input("enter c1:"))
c2=int(input("enter c2:"))

#takes the radius
radius=int(input("radius:"))   
 
def circleLocation():
    
# calculate distance to locate the point position
    dist=((x1-c1)**2+(y1-c2)**2)**1/2

    if dist<radius:
        print("given point lies inside the circle")

    elif dist>radius:
        print("the point lies outside the circle")

    elif dist==radius:
        print("the point lies inside the circle")

    else:
        print("invalid data")
        
circleLocation()



   


    