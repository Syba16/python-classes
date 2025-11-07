# Write a program to for the below:
# a. The program should take inputs for Five Subjects. English, French, Mathematics, Physics, Chemistry
# b. Maximum Marks is 500 (100 Per Subject)
# c. Calculate the Percentage Scored

eng=int(input("enter english marks:"))
#print(eng)
french=float(input("enter french marks:"))
#print(french)
math=float(input("enter math marks:"))
#print(math)
phy=float(input("enter phy:"))
#print(phy)
chem=float(input("enter chem:"))
#print(chem)

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
