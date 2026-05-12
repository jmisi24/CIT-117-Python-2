# Name: Joseph Misialek
# Assignment: SQL and Python
# Reflection:
# Share what you liked about this assignment?
#     I liked learning the SQL statements! It was something entirely different from everything we've done before,
#     and it was a good challenge to make work. I also liked it because the correlation to using it in the field is
#     very obvious.
#
# Share what you struggled with?
#     I struggled with getting the different tables to join together. I had to play around with the FROM statement...
#     Employee is the right table to have in that statement, but it feels like all 3 are supposed to be there because
#     they're all being referenced to join together.
#
# In your own words how does the DDL and DML statements work and how you used them?
#     DDL is Data Definition Language, it's used for creating the structure of the database. An example of this is,
#     "CREATE TABLE" - used to create the table that gets data inputs. DML is Data Manipulation Language, it's used for
#     moving data to/from the structure that's created with DDL. An example of this is "INSERT" - used to put data into
#     a table.
#
# In your own words describe how the SQL Select Joins work in your code?
#     The SELECT statement starts with the Employee table. The first JOIN joins the Pay table to the Employee table via
#     the Employee ID. The second JOIN statement joins the Social Security table to the Pay table via the Year. Thus,
#     creating a chain where all three tables are linked, despite there not being a direct link between the Employee
#     and Social Security tables. The FROM statement is used with the Employee table because it's the 'base' table in
#     the chain of tables.
#
# Share your top 2 things you learned on this assignment:
# 1. I learned that DDL and DML statements play different roles but they both manage the data in the database.
# 2. I learned how to use SELECT and JOIN statements to link multiple tables together.



# initials at the end of variables wasn't in the instructions, but I'll add them anyway to be safe.

import sqlite3

# Efficiency tradeoff because I need an extra loop in main() for each file import to work, but I wanted the
# reusability of the code.
# I understand that if we were working with much more data at a larger scale & higher stakes, efficiency > convenience.
def importFile(sFileNameJRM):
    fileJRM = open(sFileNameJRM, "r")
    lstRowsJRM = []
    bFirstRecordJRM = True  # skips heading row
    for sRowJRM in fileJRM:           # |
        if bFirstRecordJRM:           # |
            bFirstRecordJRM = False   # |
            continue                  # \/
        sRowJRM = sRowJRM.strip()  # cleans up row
        lstFieldsJRM = sRowJRM.split(",")  # splits row into a list of fields
        lstRowsJRM.append(lstFieldsJRM)   # appends each list of fields to larger list,
    fileJRM.close()                       # making this list ^^ compiled of each row split up by field
    return lstRowsJRM


def main():
    dbConnectionJRM = sqlite3.connect("Retirement.db")
    dbCursorJRM = dbConnectionJRM.cursor()


    # Part 1: Data Creation, Import and Insertion


    # create the 3 tables ONLY if they do not already exist
    dbCursorJRM.execute("CREATE TABLE IF NOT EXISTS Employee (EmployeeID int, Name text)")
    dbCursorJRM.execute("CREATE TABLE IF NOT EXISTS Pay (EmployeeID int,Year int,Earnings real)")
    dbCursorJRM.execute("CREATE TABLE IF NOT EXISTS SocialSecurityMin (Year int,Minimum real)")
    dbConnectionJRM.commit()

    # insert data ONLY if the tables are empty
    dbCursorJRM.execute("SELECT COUNT(*) FROM Employee")
    if dbCursorJRM.fetchone()[0] == 0:

        # import Employee.txt and insert fields
        for lstFieldsJRM in importFile("Employee.txt"):
            iEmployeeIDJRM = int(lstFieldsJRM[0])
            sNameJRM = lstFieldsJRM[1]
            sInsertEmployeeJRM = f"INSERT INTO Employee(EmployeeID, Name) VALUES({iEmployeeIDJRM}, '{sNameJRM}')"
            dbCursorJRM.execute(sInsertEmployeeJRM)

        # import Pay.txt and insert fields
        for lstFieldsJRM in importFile("Pay.txt"):
            iEmployeeIDJRM = int(lstFieldsJRM[0])
            iYearJRM = int(lstFieldsJRM[1])
            fEarningsJRM = float(lstFieldsJRM[2])
            sInsertPayJRM = (f"INSERT INTO Pay(EmployeeID, Year, Earnings) \
                               VALUES({iEmployeeIDJRM}, {iYearJRM}, {fEarningsJRM})")
            dbCursorJRM.execute(sInsertPayJRM)

        # import SocialSecurityMinimum.txt and insert fields
        for lstFieldsJRM in importFile("SocialSecurityMinimum.txt"):
            iYearJRM = int(lstFieldsJRM[0])
            fMinimumJRM = float(lstFieldsJRM[1])
            sInsertSSMinJRM = f"INSERT INTO SocialSecurityMin(Year, Minimum) VALUES({iYearJRM}, {fMinimumJRM})"
            dbCursorJRM.execute(sInsertSSMinJRM)

    dbConnectionJRM.commit()


    # Part 2: Data Reporting


    # join all 3 tables, Employee to Pay via EmployeeID, and Pay to SocialSecurityMin via Year
    sSQLSelectJRM = """
        SELECT Employee.EmployeeID,
            Employee.Name,
            Pay.Year,
            Pay.Earnings,
            SocialSecurityMin.Minimum
        FROM Employee
        JOIN Pay ON Employee.EmployeeID = Pay.EmployeeID
        JOIN SocialSecurityMin ON Pay.Year = SocialSecurityMin.Year
        ORDER BY Employee.Name, Pay.Year
    """
    dbCursorJRM.execute(sSQLSelectJRM)

    # header for output
    print("")
    print(f"{'ID':<5} {'Name':<25} {'Year':<25} {'Earnings':<25} {'Minimum':<25} {'Include':<25}")
    print("-" * 120)

    # process each row for output and to determine retirement eligibility for that year
    for tupSQLRowsJRM in dbCursorJRM.fetchall():
        iEmployeeIDJRM = tupSQLRowsJRM[0]
        sNameJRM = tupSQLRowsJRM[1]
        iYearJRM = tupSQLRowsJRM[2]
        fEarningsJRM = tupSQLRowsJRM[3]
        fMinimumJRM = tupSQLRowsJRM[4]

        if fEarningsJRM >= fMinimumJRM:
            sEligibleJRM = "Yes"
        else:
            sEligibleJRM = "No"

        print(f"{iEmployeeIDJRM:<5} {sNameJRM:<25} {iYearJRM:<25} {fEarningsJRM:<25,.2f} \
{fMinimumJRM:<25,.2f} {sEligibleJRM:<25}")

    dbConnectionJRM.close()

main()