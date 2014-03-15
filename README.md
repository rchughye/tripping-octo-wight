tripping-octo-wight
===================
Primary purpose is to act as a portfolio of sorts.

Currently includes: a back end prototype of data mining software (Cobb Public.py) and Project Euler problems

.py scripts were made for Python Version 2.6

rchughye@uwaterloo.ca
3/6/2014




Cobb.py
===================

OVERVIEW:
On: http://www.cobbsheriff.org/inmate/JMS_Admit_Review.asp?
Goes onto the Cobb County website and mines inmate data into readable excel file
with the following output in columns:
Last Name, First Name, Address, City, State, Zip, Charge, and Charge Type (Felony or Misdemeanor)

Usage:
When executed, will ask for begin date and end date in format mm/dd/yyyy hh:mm
Will automatically write to the directory of the .exe

Process:
Parses user input for desired dates of inmate information,
searches the appropriate site URL with that information (with appropriate cookie manipulation),
iteratively mines information from the table presented.
(Assumes a format with table numbers/positions currently valid at 2/26/2014)
Note for user/testing: Website limits searches only up to a span of 3 days. Empty output provided otherwise


Libraries:
===================
beautiful soup v4.1
http://www.crummy.com/software/BeautifulSoup/bs4/download/4.1/


Project Euler
===================
http://projecteuler.net/problems

Problems that were particularly interesting to me:

Problem 11: matrix representation of numbers

Problem 12: requiring efficiency improvements to get a reasonable runtime from the naive implementation

Problem 17: string parsing

Problem 19: date and string parsing

All solutions and commented thought processes within the code are my own work
