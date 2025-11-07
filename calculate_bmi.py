name=input("enter your name: ")
height=float(input("enter your height in meters: "))
weight=float(input("enter your weight in kgs: "))

bmi=weight/height**2

if(bmi<=18.5):

    print("name:",name,
          "\nHeight:",height,
          "\nWeight:",weight,
          "\nBMI:",bmi,
          "\n You are underweight")
    
elif(bmi>18.5 and bmi<=24.9):
          
        print("name:",name,
          "\nHeight:",height,
          "\nWeight:",weight,
          "\nBMI:",bmi,
          "\n You are Normal") 
        
elif(bmi>25.0 and bmi<=29.9):
          
        print("name:",name,
          "\nHeight:",height,
          "\nWeight:",weight,
          "\nBMI:",bmi,
          "\n You are Overweight") 
        
elif(bmi>30.0 and bmi<=34.9):
          
        print("name:",name,
          "\nHeight:",height,
          "\nWeight:",weight,
          "\nBMI:",bmi,
          "\n You are obese") 

elif(bmi>35.0 and bmi<=39.9):
          
        print("name:",name,
          "\nHeight:",height,
          "\nWeight:",weight,
          "\nBMI:",bmi,
          "\n You are obese") 
        
elif(bmi>=40):
          
        print("name:",name,
          "\nHeight:",height,
          "\nWeight:",weight,
          "\nBMI:",bmi,
          "\n You are Extremely Obese") 
else:
    print("invalid input")
    
