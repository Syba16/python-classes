#Write a function that calculates the below: ( Mathematics - Geometry) 
#Area of the Circle
#Circumference of the Circle
#Volume and Surface area of a Cylinder
#Area of the rectangle
#Perimeter of the rectangle
#Area of the Square



radius = float(input("radius: "))
area_cir = 3.14 * radius * radius
circumference = 2 * 3.14 * radius
print("Area of Circle: ", area_cir)
print("Circumference of Circle: ", circumference)

# Volume and Surface area of Cylinder
height=float(input("enter height:"))
volume=3.14*radius*radius*height
Sur_area=2*3.14*radius*height+2*3.14*radius*radius
print("Volume of Cylinder:",volume,"Surface Area of Cylinder:",Sur_area)

#area and perimeter of a rectangle
length=float(input("enter length:"))
breadth=float(input("enter breadth:"))
area_rec=length*breadth
peri=2*(length+breadth)
print("area of rectangle:",area_rec,"\nperimeter of rectangle:",peri)

#area of square
side=float(input("side="))
area_sq=side*side
print("area of square:",area_sq)