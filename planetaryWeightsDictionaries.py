# Name: Joseph Misialek
# Assignment: Planetary Weights Dictionaries
# Reflection:
# Share what you liked about the assignment?
#    I liked incorporating the dictionaries into the code. It gives a good idea of how they can be used
#    and gives a practical application of it.
# Share what you struggled with?
#    I struggled with formatting the final output. It had been a while since I've used the f-string modifiers
#    and I definitely had to give myself a refresher on how they work.
# How did you like working with dictionaries and pickling concepts?
#    I enjoyed working with dictionaries and pickling. They certainly feel more advanced compared to Python 1 and
#    make me wonder what is to come with future topics.
# Share exactly 2 things you learned on this assignment:
# 1. I learned how to create a dictionary and modify one within my code.
# 2. I learned how to use pickling to keep a history of previous code results.

import pickle

def main():
    dictPlanetaryConversionsJRM = {
        'Mercury': 0.38,
        'Venus': 0.91,
        'Moon': 0.165,
        'Mars': 0.38,
        'Jupiter': 2.34,
        'Saturn': 0.93,
        'Uranus': 0.92,
        'Neptune': 1.12,
        'Pluto': 0.066
    }

    # Open pickling file, perform error checking, and transfer into dictionary
    dictPlanetHistoryJRM = {}
    eofJRM = False
    try:
        input_fileJRM = open('jmPlanetaryWeights.db', 'rb')
        while not eofJRM:
            try:
                dictPlanetHistoryJRM = pickle.load(input_fileJRM)
            except EOFError:
                eofJRM = True
        input_fileJRM.close()
    except FileNotFoundError:
        pass

    # Prompt user to see previous entries
    sSeeHistoryJRM = input("Would you like to see the previous entries (y or n)?: ").lower()
    if sSeeHistoryJRM == 'y':
        for sNameJRM, fWeightsJRM in dictPlanetHistoryJRM.items():
            print(f"{sNameJRM}, here are your weights on our Solar System's planets:")
            for sPlanetJRM, fOutputtedWeight in fWeightsJRM.items():
                print(f"Weight on {sPlanetJRM + ':':25s} {fOutputtedWeight:10.2f}")

    # Input loop
    while True:
        sNameJRM = input("Enter name (leave blank to exit): ").capitalize()
        # If name is not inputted, stop the code.
        if not sNameJRM:
            break
        # Check if name exists in dictPlanetHistoryJRM
        if sNameJRM.lower() in [sKeyJRM.lower() for sKeyJRM in dictPlanetHistoryJRM]:
            print(f"'{sNameJRM}' is already in the history file. Enter a unique name.")
            continue
        # Prompt for Earth Weight with error handling
        while True:
            try:
                fEarthWeightJRM = float(input(f"Enter {sNameJRM}'s Earth Weight: "))
                break
            except ValueError:
                print("Not a number. Please enter a valid number.")
        # Declare new dictionary
        dictNewPersonWeightsJRM = {}
        # Create another loop to calculate weight on each planet. Then store to dictionary
        print(f"{sNameJRM}, here are your weights on our Solar System's planets:")
        for sPlanetJRM, fFactorJRM in dictPlanetaryConversionsJRM.items():
            fPlanetWeight = fEarthWeightJRM * fFactorJRM
            dictNewPersonWeightsJRM[sPlanetJRM] = fPlanetWeight
            print(f"Weight on {sPlanetJRM + ':':25s} {fPlanetWeight:10.2f}")

        # Add person's weight to history dictionary
        dictPlanetHistoryJRM[sNameJRM] = dictNewPersonWeightsJRM

    # Output file
    output_fileJRM = open('jmPlanetaryWeights.db', 'wb')
    pickle.dump(dictPlanetHistoryJRM, output_fileJRM)
    output_fileJRM.close()

main()
