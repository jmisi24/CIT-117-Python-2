#Name: Joseph Misialek
#Assignment: Numerology Class
#Reflection:
#Share what you liked about the assignment?:
# I liked this assignment because it was challenging. Every step of the way I ran into a speed bump, even trying to
# use the class from the other file in the use file. I enjoy the challenge and problem-solving that comes with it.
#
#Share what you struggled with?:
# I struggled with validating the format of the date. I initially started with a different library but couldn't get it
# to work the way I wanted, so I pivoted to a different one that is confusing, but it works. I also struggled with the
# logic behind reducing the date and such.
#
#Think back to a previous assignment, how could you rewrite it to use Python classes?:
# I could code a class into the interplanetary weight assignment. Making separate objects for the name, earth weight,
# calculations, display, etc.
#
#Share exactly 2 things you learned on this assignment:
# 1.) I learned how to create a class and objects.
# 2.) I learned how to protect my code by encapsulating using dunders __xxxx__



class Numerology:
    def __init__(self, sNameJRM, sDOBJRM):          #initialize class and pass parameters
        self.__name = sNameJRM          #encapsulate name so it is private
        self.__dob = sDOBJRM            #encapsulate dob so it is private

    def getName(self):          #getter for name, should be a property
        return self.__name

    def getBirthdate(self):         #getter for dob, should be a property
        return self.__dob

    def getAttitude(self):
        lstDOBPartsJRM = self.__dob.split('-') if '-' in self.__dob else self.__dob.split('/')      #split dob format
        iDOBMonthJRM = lstDOBPartsJRM[0]            #declare which part of the list is month
        iDOBDayJRM = lstDOBPartsJRM[1]              #declare which part of the list is day
        iTotalJRM = sum(int(iDigitsJRM) for iDigitsJRM in iDOBMonthJRM + iDOBDayJRM)        #add total digits of m/d
        return self.__reduce(iTotalJRM)         #reduce to single digit number & return

    def getBirthDay(self):
        lstDOBPartsJRM = self.__dob.split('-') if '-' in self.__dob else self.__dob.split('/')      #split dob format
        iDOBDayJRM = lstDOBPartsJRM[1]          #declare which part of the list is day
        iTotalJRM = sum(int(iDigitsJRM) for iDigitsJRM in iDOBDayJRM)           #add total digits of day
        return self.__reduce(iTotalJRM)         #reduce to single digit number & return

    def getLifePath(self):
        iDOBDigitsJRM = self.__dob.replace('-', '').replace('/', '')        #replace format so dob is only numbers
        iTotalJRM = sum(int(iDigitsJRM) for iDigitsJRM in str(iDOBDigitsJRM))        #total all digits in dob
        return self.__reduce(iTotalJRM)             #reduce to single digit number & return

    def getPersonality(self):
        sVowelsJRM = set('aeiouAEIOU')          #create set for vowels for efficiency and because they won't change
        #create loop to find constants in name by referencing vowel set
        sConsonantsJRM = [sCharacterJRM for sCharacterJRM in self.__name if sCharacterJRM not in sVowelsJRM]
        #total all digits from consonant to number conversion
        iTotalJRM = sum(self.__letterToNumber(sCharacterJRM) for sCharacterJRM in sConsonantsJRM)
        return self.__reduce(iTotalJRM)         #reduce to single digit number & return

    def getPowerName(self):
        iTotalJRM = self.getSoul() + self.getPersonality()      #add soul and personality numbers together
        return self.__reduce(iTotalJRM)         #reduce to single digit number & return

    def getSoul(self):
        sVowelsJRM = set('aeiouAEIOU')          #create set for vowels for efficiency and because they won't change
        #reference each character in name to the vowel set to determine whether it's a vowel or consonant
        sIncludedVowelsJRM = [sCharacterJRM for sCharacterJRM in self.__name if sCharacterJRM in sVowelsJRM]
        #total all digits from vowel to number conversion
        iTotalJRM = sum(self.__letterToNumber(sCharacterJRM) for sCharacterJRM in sIncludedVowelsJRM)
        return self.__reduce(iTotalJRM)         #reduce to single digit number & return

    def __letterToNumber(self, sCharacterJRM):      #private because we want it immutable for accurate conversions
        sCharacterJRM = sCharacterJRM.upper()       #capitalizes for consistency
        dictMappingJRM = {                          #create dictionary for referencing value per character
            'A': 1, 'J': 1, 'S': 1,
            'B': 2, 'K': 2, 'T': 2,
            'C': 3, 'L': 3, 'U': 3,
            'D': 4, 'M': 4, 'V': 4,
            'E': 5, 'N': 5, 'W': 5,
            'F': 6, 'O': 6, 'X': 6,
            'G': 7, 'P': 7, 'Y': 7,
            'H': 8, 'Q': 8, 'Z': 8,
            'I': 9, 'R': 9
        }
        return dictMappingJRM.get(sCharacterJRM, 0)

    def __reduce(self, iNumberJRM):         #private because we want it immutable for accurate number reductions
        while iNumberJRM > 9:               #loop to continue reducing the number until it's single digit
            iNumberJRM = sum(int(iDigitsJRM) for iDigitsJRM in str(iNumberJRM))
        return iNumberJRM
