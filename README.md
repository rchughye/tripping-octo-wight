tripping-octo-wight
===================
Currently for the sole purpose of displaying the Cobb.py code.

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

rchughye@uwaterloo.ca or ilikepi3@gmail.com
2/26/2014

Libraries:
===================
beautiful soup v4.1
http://www.crummy.com/software/BeautifulSoup/bs4/download/4.1/
