#Name: Joseph Misialek
#Assignment: Numerology Inheritance
#Reflection:
#Share what you liked about the assignment?:
# I liked learning how to inherit a class within a class. Why you would do it makes sense, and it makes the code
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



class Numerology:
    def __init__(self, sNameJRM, sDOBJRM):
        self.__sNameJRM = sNameJRM
        self.__iDobJRM = sDOBJRM

        #combine computing into __init__ - per feedback on last assignment

        #splits the dob into a list with day and month specified to be used by other calculations.
        lstPartsJRM = sDOBJRM.split('-') if '-' in sDOBJRM else sDOBJRM.split('/')
        sMonthJRM = lstPartsJRM[0]
        sDayJRM   = lstPartsJRM[1]

        #splits the name into a list of the vowels and consonants to be used by other calculations.
        sVowelsJRM = set('aeiouAEIOU')
        lstVowelsJRM     = [sCharacterJRM for sCharacterJRM in sNameJRM if sCharacterJRM in sVowelsJRM]
        lstConsonantsJRM = [sCharacterJRM for sCharacterJRM in sNameJRM if sCharacterJRM.isalpha() and
                            sCharacterJRM not in sVowelsJRM]

        #pre-compute all six numbers and store them privately - per feedback
        self.__iAttitudeNumberJRM = self.__reduce(sum(int(iDigitsJRM) for iDigitsJRM in sMonthJRM + sDayJRM))
        self.__iBirthdayNumberJRM = self.__reduce(sum(int(iDigitsJRM) for iDigitsJRM in sDayJRM))
        self.__iLifePathNumberJRM = self.__reduce(sum(int(iDigitsJRM) for iDigitsJRM in
                                                      sDOBJRM.replace('-','').replace('/','')))
        self.__iSoulNumberJRM = self.__reduce(sum(self.__charToInt(sCharacterJRM) for sCharacterJRM in lstVowelsJRM))
        self.__iPersonalityNumberJRM = self.__reduce(sum(self.__charToInt(sCharacterJRM) for sCharacterJRM in
                                                         lstConsonantsJRM))
        self.__iPowerNameNumberJRM = self.__reduce(self.__iSoulNumberJRM + self.__iPersonalityNumberJRM)

    #getters with decorators making them all into properties. values pre-computed in __init__
    @property
    def Name(self):
        return self.__sNameJRM
    @property
    def Birthdate(self):
        return self.__iDobJRM
    @property
    def Attitude(self):
        return self.__iAttitudeNumberJRM
    @property
    def BirthDay(self):
        return self.__iBirthdayNumberJRM
    @property
    def LifePath(self):
        return self.__iLifePathNumberJRM
    @property
    def Soul(self):
        return self.__iSoulNumberJRM
    @property
    def Personality(self):
        return self.__iPersonalityNumberJRM
    @property
    def PowerName(self):
        return self.__iPowerNameNumberJRM

    #ASCII/Unicode character to integer calculation - per feedback
    def __charToInt(self, sCharJRM):
        return ((ord(sCharJRM.upper()) - 65) % 9 + 1) if sCharJRM.isalpha() else 0

    #__reduce simpler calculation - per feedback
    def __reduce(self, iNumberJRM):
        while len(str(iNumberJRM)) > 1:
            iNumberJRM = (iNumberJRM % 10) + (iNumberJRM // 10)
        return iNumberJRM

#create new class that inherits the original
class NumerologyLifePathDetails(Numerology):
    def __init__(self, sNameJRM, sDOBJRM):
        Numerology.__init__(self, sNameJRM, sDOBJRM)         #to run the __init__ of the Numerology class

    #getter with decorator
    @property
    def LifePathDescription(self):
        dictDescriptionsJRM = {
            1: "The Independent: Wants to work/think for themselves",
            2: "The Mediator: Avoids conflict and wants love and harmony",
            3: "The Performer: Likes music, art and to perform or get attention",
            4: "The Teacher/Truth Seeker: Is meant to be a teacher or mentor and is truthful",
            5: "The Adventurer: Likes to travel and meet others, often an extrovert",
            6: "The Inner Child: Is meant to be a parent and/or one that is young at heart",
            7: "The Naturalist: Enjoy nature and water and alternative life paths, open to spirituality",
            8: "The Executive: Gravitates to money and power",
            9: "The Humanitarian: Helps others and/or experiences pain and learns the hard way"
        }
        return dictDescriptionsJRM.get(self.LifePath)