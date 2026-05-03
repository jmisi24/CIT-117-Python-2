# Name: Joseph Misialek
# Assignment: Password Validator
# Reflection:
#  Share what you liked about this assignment?
#       This assignment was challenging. It's been a year since I took Python 1, so I really felt that I was able to
#       break off the rust with this project and that's a great feeling. Getting used to using functions, lists,
#       if/else, and loops was a great refresher.
#  Share what you struggled with?
#       I struggled with consolidating the code so that it runs more efficiently, and with making my loops work
#       appropriately. A lot of trial and error, but it's good practice.
#  How did you write your code to be efficient and reduce redundancy?
#       I consolidated the uppercase, lowercase, number, and special character checks into one loop rather than four
#       separate ones. I also consolidated the length requirement to using the len() function once, so that it didn't
#       have to take the length of the variable twice.
#  Share exactly 2 things you learned on this assignment:
#   1. I learned how much more malleable string functions can make your code.
#   2. I learned the impact commentating makes on the more tricky lines of code and how much it helps ease
#      understanding as well as make referencing quicker.


# main function
def main():
    # prompt user for name
    sNameJRM = input("Enter full name such as 'John Smith': ").split()   # splits into list of strings based on spaces

    # identify and store initials based off of name
    sInitialsJRM = f'{sNameJRM[0][0]}{sNameJRM[1][0]}'     # stores the first character of the first and second items
                                                           # in the list created above
    bValidPasswordJRM = False      # to set up for the while loop
    while not bValidPasswordJRM:       # loop continues as long as bValidPasswordJRM is False
        SPECIAL_CHARACTERS = '!@#$%^'       # constant for special characters

        # prompt user for password
        sPasswordJRM = input('Enter desired password: ')

        bValidPasswordJRM = True   # assume it's valid unless it doesn't pass a rule

        # VALIDATING

        # length requirement
        if not (8 <= len(sPasswordJRM) <= 12): #if len(sPasswordJRM) >= 8 or len(sPasswordJRM) <= 12:
            print('Password must be between 8 and 12 characters.')
            bValidPasswordJRM = False

        # can't start with pass
        if sPasswordJRM.lower().startswith('pass'):
            print("Password can't start with Pass.")
            bValidPasswordJRM = False

        # initials checking
        if sInitialsJRM.lower() in sPasswordJRM.lower():
            print('Password must not contain user initials.')
            bValidPasswordJRM = False

        # uppercase, lowercase, number, and special character checking
        bUppercaseJRM = False      # prep for the for loop
        bLowercaseJRM = False      # consolidated this into one loop after watching the lecture!
        bNumberJRM = False
        bHasSpecCharacterJRM = False
        for sLetter in sPasswordJRM:
            if sLetter.isupper():
                bUppercaseJRM = True
            elif sLetter.islower():
                bLowercaseJRM = True
            elif sLetter.isdigit():
                bNumberJRM = True
            elif sLetter in SPECIAL_CHARACTERS:
                bHasSpecCharacterJRM = True

        # these will trigger if the respective variables are still 'False' indicating the password didn't meet a rule
        if not bUppercaseJRM:
            print('Password must contain at least 1 uppercase letter.')
            bValidPasswordJRM = False
        if not bLowercaseJRM:
            print('Password must contain at least 1 lowercase letter.')
            bValidPasswordJRM = False
        if not bNumberJRM:
            print('Password must contain at least 1 number.')
            bValidPasswordJRM = False
        if not bHasSpecCharacterJRM:
            print(f'Password must contain at least 1 of these special characters: {SPECIAL_CHARACTERS}')
            bValidPasswordJRM = False

        # duplicate character checking
        sCharactersCheckedJRM = ''     # to store the letter's we've already checked to avoid duplicate outputs
        bPrintHeaderJRM = False
        for sCharacter in sPasswordJRM.lower():
            if sCharacter not in sCharactersCheckedJRM:
                iCountJRM = sPasswordJRM.lower().count(sCharacter)      # keeps count of how many of each letter
                if iCountJRM > 1:
                    if not bPrintHeaderJRM:
                        print('These characters appear more than once: ')
                        bPrintHeaderJRM = True
                    print(f'{sCharacter}: {iCountJRM} times')       # print each character that appeared more than once
                    sCharactersCheckedJRM += sCharacter     # add checked characters to variable storing them
                    bValidPasswordJRM = False

        # results
        if bValidPasswordJRM == True:
            print('Password is valid and OK to use.')
        else:
            print('TRY AGAIN!')
main()