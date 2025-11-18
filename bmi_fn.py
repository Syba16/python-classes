import time

name=input("enter your name: ")
gender=input("what's your gender: ").lower()
h=float(input("enter your height in meters: "))
weight=float(input("enter your weight in kgs: "))

height=h*0.304 #converting into feet
bmi_m=weight/height**2
bmi_f=weight/703*height**2

def func_bmi():

    if gender=="m" or 'male':
        bmi=bmi_m
    else:    
        bmi=bmi_f
        
    if(bmi<=18.5):
        time.sleep(1)
        print("name:",name,
            "\nHeight:",height,
            "\nWeight:",weight,
            "\nBMI:",bmi,
            "\n You are underweight")
        
    elif(bmi>18.5 and bmi<=24.9):
        time.sleep(1)    
        print("name:",name,
            "\nHeight:",height,
            "\nWeight:",weight,
            "\nBMI:",bmi,
            "\n You are Normal") 
            
    elif(bmi>25.0 and bmi<=29.9):
        time.sleep(1)    
        print("name:",name,
            "\nHeight:",height,
            "\nWeight:",weight,
            "\nBMI:",bmi,
            "\n You are Overweight") 
            
    elif(bmi>30.0 and bmi<=34.9):
        time.sleep(1)   
        print("name:",name,
        "\nHeight:",height,
        "\nWeight:",weight,
        "\nBMI:",bmi,
        "\n You are obese") 

    elif(bmi>35.0 and bmi<=39.9):
            time.sleep(1)
            print("name:",name,
            "\nHeight:",height,
            "\nWeight:",weight,
            "\nBMI:",bmi,
            "\n You are obese") 
            
    elif(bmi>=40):
        time.sleep(1)    
        print("name:",name,
            "\nHeight:",height,
            "\nWeight:",weight,
            "\nBMI:",bmi,
            "\n You are Extremely Obese") 
    else:
        time.sleep(1)
        print("invalid input")


func_bmi()