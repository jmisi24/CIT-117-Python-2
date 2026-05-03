#Name: Joseph Misialek
#Assignment: Numerology Inheritance
#Reflection:
#Share what you liked about the assignment?:
# I liked learning how to inherit a class from a class. Why you would do it makes sense, and it makes the code
# infinitely expandable without having to alter what's already been written. I did also enjoy implementing the feedback
# from the last assignment. Making the code more efficient is always fun to grapple with and takes plenty of critical
# thinking.

#Share what you struggled with?:
# I struggled with understanding properties and decorators. I had to re-watch the lecture multiple times over the course
# of a few days to make it make sense. It's interesting because it doesn't seem like a super complicated concept, but I
# just couldn't seem to make it make sense.

#In your own words describe how decoration works & how does it help coders write better code?:
# Decorators are used to change how Python handles a function without having to alter the function itself. This helps
# coders write better code because it gives them versatility. They can make code read-only, or convert it into a setter,
# making code more efficient and avoid excess code.

#Share exactly 2 things you learned on this assignment:
# 1.) I learned how to inherit a class from another class, and how to make sure it runs the __init__ of the parent.
# 2.) I learned what a property was, how it's used within code, and how to implement them using decorators.



from NumerologyLifePathDetails import NumerologyLifePathDetails
import re

def getValidDate():
    while True:
        sDOBJRM = input("Enter your birth date (mm-dd-yyyy or mm/dd/yyyy): ").strip()       #inquire and clean up DOB
        sDOBFormatJRM = r"^\d{2}[-/]\d{2}[-/]\d{4}$"        #specifies dob format
        if re.match(sDOBFormatJRM, sDOBJRM):            #validates dob format
            return sDOBJRM
        else:           #throws error if format is wrong
            print("Invalid date format. Please enter a full 8-digit date (mm-dd-yyyy or mm/dd/yyyy).")

def getValidName():
    while True:
        sNameJRM = input("Enter your full birth name: ").strip()        #inquire and clean up name
        if sNameJRM:
            return sNameJRM
        else:           #validates name isn't empty. throws error if it is.
            print("Name cannot be empty. Please enter your name.")

def main():
    print("\n-=--=--=--=--=--=--=--=--=--=--=--=--=--=--=-")
    print("       Welcome to the Numerology Reader")
    print("-=--=--=--=--=--=--=--=--=--=--=--=--=--=--=-\n")

    sNameJRM = getValidName()
    sDOBJRM  = getValidDate()

    #calls new Class that's inheriting the original
    oOutputJRM = NumerologyLifePathDetails(sNameJRM, sDOBJRM)

    print("\n===================================================")
    print("         Your Numerology Reading")
    print("===================================================\n")
    print(f"Name            : {oOutputJRM.Name}")
    print(f"Birth Date      : {oOutputJRM.Birthdate}")
    print(f"Life Path Number: {oOutputJRM.LifePath}")
    print(f"Birth Day Number: {oOutputJRM.BirthDay}")
    print(f"Attitude Number : {oOutputJRM.Attitude}")
    print(f"Soul Number     : {oOutputJRM.Soul}")
    print(f"Personality Num : {oOutputJRM.Personality}")
    print(f"Power Name Num  : {oOutputJRM.PowerName}")
    print(f"\nLife Path Meaning : {oOutputJRM.LifePathDescription}")
    print("\n===================================================")


main()