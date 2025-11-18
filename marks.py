# Write a program to for the below using functions:
# a. The program should take inputs for Five Subjects. English, French, Mathematics, Physics, Chemistry
# b. Maximum Marks is 500 (100 Per Subject)
# c. Calculate the Percentage Scored

eng=int(input("enter english marks:"))
french=float(input("enter french marks:"))
math=float(input("enter math marks:"))
phy=float(input("enter phy:"))
chem=float(input("enter chem:"))

def marks1():
    print("\n marks scored in Final Exams:")
    print("_______________________________")
    print("English  French  Math  Physics  Chemistry")
    print("___________________________________________")
    print(eng,"\t",french,"\t",math,"\t",phy,"\t",chem)
    print("__________________________________________")
    total=eng+french+math+phy+chem
    print("Total Marks:",total)
    percentage=(total/500)*100
    print("Percentage:",percentage)

marks1()