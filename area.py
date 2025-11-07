# calculating area using functions

def area_circle():
    
    radius = float(input("radius: "))
    area_cir = 3.14 * radius * radius
    circumference = 2 * 3.14 * radius
    print("Area of Circle: ", area_cir)
    print("Circumference of Circle: ", circumference)

def area_circle2(radius):
    
    #radius = float(input("radius: "))
    area_cir = 3.14 * radius * radius
    circumference = 2 * 3.14 * radius
    #print("\nArea of Circle: ", area_cir)
    #print("\nCircumference of Circle: ", circumference)
    return area_cir,circumference

def vol_cylinder():
    
    radius = float(input("radius: "))
    height=float(input("enter height:"))
    volume=3.14*radius*radius*height
    Sur_area=2*3.14*radius*height+2*3.14*radius*radius
    print("\nVolume of Cylinder:",volume,"\nSurface Area of Cylinder:",Sur_area)

def vol_cylinder2(radius,height):
    
    #radius = float(input("radius: "))
    #height=float(input("enter height:"))
    volume=3.14*radius*radius*height
    sur_area=2*3.14*radius*height+2*3.14*radius*radius
    #print("\nVolume of Cylinder:",volume,"\nSurface Area of Cylinder:",Sur_area)
    return volume,sur_area

def area_rectangle(): 
    
    length=float(input("enter length:"))
    breadth=float(input("enter breadth:"))
    area_rec=length*breadth
    peri=2*(length+breadth)
    print("\narea of rectangle:",area_rec,"\nperimeter of rectangle:",peri)

def area_rectangle2(length,breadth): 
    
    #length=float(input("enter length:"))
    #breadth=float(input("enter breadth:"))
    area_rec=length*breadth
    peri=2*(length+breadth)
    #print("\narea of rectangle:",area_rec,"\nperimeter of rectangle:",peri)
    return area_rec,peri

def area_square():
    side=float(input("side="))
    area_sq=side*side
    print("\narea of square:",area_sq)

def area_square2(side):
    #side=float(input("side="))
    area_sq=side*side
    #print("\narea of square:",area_sq)
    return area_sq