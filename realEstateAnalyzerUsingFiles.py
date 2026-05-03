# Name: Joseph Misialek
# Assignment: Real Estate Analyzer Using Files, Lists, and Dictionaries
# Reflection:
# Share what you liked about this assignment?
#    One thing I liked about this assignment was it felt very structurally sound, and it made sense putting everything
#    where I did. It's a nice workflow.
# Share what I struggled with?:
#    I struggled with getting the .csv to import appropriately, and I also struggled with sorting specific columns
#    out to their respective dictionaries/lists.
# Which approach did I use to import the data and why did I choose it?:
#    I chose the approach that uses the Path library and csv.reader as I found it the easiest, most consolidated,
#    and it was also easy to chop off the header row in the .csv
# How many dictionaries did I use?:
#    I used 3 dictionaries in this code. One for City Totals, Zip Totals, and Property Type Totals.
# Share exactly 2 things I learned from this assignment:
#   1. I learned how to import a .csv file into a program and manipulate the data afterward.
#   2. I learned the reasoning behind finding a median without importing a library.

import csv
from pathlib import Path

def getDataInput():
    dataFileJRM = Path('RealEstateData.csv')
    with dataFileJRM.open(mode='r') as fileJRM:
        return list(csv.reader(fileJRM))[1:]        # [1:] chops off the header in the csv that doesn't contain data

def getMedian(lstPricesJRM):
    iListLengthJRM = len(lstPricesJRM)      # total # of entries in list
    iMiddleOfListJRM = iListLengthJRM // 2      # finds middle entry to help find median

    if iListLengthJRM % 2 == 1:     # if it has a remainder of 1 when dividing by 2, it's odd
        return float(lstPricesJRM[iMiddleOfListJRM])
    else:       # need to take the average of the middle entry and the one before
        fAverageJRM = (lstPricesJRM[iMiddleOfListJRM] + lstPricesJRM[iMiddleOfListJRM - 1]) / 2
        return fAverageJRM

def main():
    lstRealEstateJRM = getDataInput()       # pull list

    # set up lists and dictionaries for loop to sort fields
    lstPropertyPricesJRM = []
    dictCityTotalsJRM = {}
    dictZipTotalsJRM = {}
    dictTypeTotalsJRM = {}

    for itemJRM in lstRealEstateJRM:
        sCityJRM = itemJRM[1]               # extracts city column from list
        sPropertyTypeJRM = itemJRM[7]       # extracts property type column from list
        sZipJRM = itemJRM[2]                # extracts zip code column from list
        fPriceJRM = float(itemJRM[8])       # extracts price column from list and converts to float

        lstPropertyPricesJRM.append(fPriceJRM)      # adds prices to price list

        # update dictionary totals
        dictCityTotalsJRM[sCityJRM] = dictCityTotalsJRM.get(sCityJRM, 0) + fPriceJRM
        dictZipTotalsJRM[sZipJRM] = dictZipTotalsJRM.get(sZipJRM, 0) + fPriceJRM
        dictTypeTotalsJRM[sPropertyTypeJRM] = dictTypeTotalsJRM.get(sPropertyTypeJRM, 0) + fPriceJRM

    lstPropertyPricesJRM.sort()     # sorts from smallest to largest, also needed for median function

    # statistics
    fMinJRM = min(lstPropertyPricesJRM)
    fMaxJRM = max(lstPropertyPricesJRM)
    fTotalJRM = sum(lstPropertyPricesJRM)
    fAveragePriceJRM = fTotalJRM / len(lstPropertyPricesJRM)

    # call median function
    fMedianJRM = getMedian(lstPropertyPricesJRM)

    # statistics output
    print("--== Statistics ==--")
    print(f"{"Minimum: ":10s}${fMinJRM:,.2f}")
    print(f"{"Maximum: ":10s}${fMaxJRM:,.2f}")
    print(f"{"Total:   ":10s}${fTotalJRM:,.2f}")
    print(f"{"Average: ":10s}${fAveragePriceJRM:,.2f}")
    print(f"{"Median:  ":10s}${fMedianJRM:,.2f}")

    # city output
    print("\n--== Summary by City ==--")
    for sCityJRM,fPriceJRM in dictCityTotalsJRM.items():
        print(f"{sCityJRM:<20} ${fPriceJRM:>15,.2f}")

    # zip output
    print("\n--== Summary by Zip Code ==--")
    for sZipJRM, fPriceJRM in dictZipTotalsJRM.items():
        print(f"{sZipJRM:<20} ${fPriceJRM:>15,.2f}")

    # property type output
    print("\n--== Summary by Property Type ==--")
    for sPropertyTypeJRM, fPriceJRM in dictTypeTotalsJRM.items():
        print(f"{sPropertyTypeJRM:<20} ${fPriceJRM:>15,.2f}")


main()