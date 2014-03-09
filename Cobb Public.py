# Cobb Public.py (WORKING BACK-END PROTOTYPE)

# Changelog v1.4 2/26/2014
# Sample for public viewing: valid as of 2/26/2014 from 

# Changelog v1.2 6/11/2013
# Tested that table 9 or 10 could contain the charge information; adjusted to search for misdimeanor or felony
# Adjusted name assuming name in form of last first middle

# Changelog v1.1
# Added data sanitation for address and zip

# OVERVIEW:
# On: http://www.cobbsheriff.org/inmate/JMS_Admit_Review.asp?
# Goes onto the Cobb County website and mines inmate data into readable excel file
# with the following output in columns: 
# Last Name, First Name, Address, City, State, Zip, Charge, and Charge Type (Felony or Misdemeanor)

# Usage: 
# When executed, will ask for begin date and end date in format mm/dd/yyyy hh:mm
# Will automatically write to the directory of the .exe

# Process: 
# Parses user input for desired dates of inmate information, 
# searches the appropriate site URL with that information (with appropriate cookie manipulation),
# iteratively mines information from the table presented. 
# (Assumes a format with table numbers/positions currently valid at 2/26/2014)
# Note for user/testing: Website limits searches only up to a span of 3 days. Empty output provided otherwise

# rchughye@uwaterloo.ca or ilikepi3@gmail.com
# 2/26/2014


import urllib2
from bs4 import BeautifulSoup
from urllib2 import Request, build_opener, HTTPCookieProcessor, HTTPHandler
import cookielib
import re

def splitter(date, num, form):
    #date is date in string form, in form "mm/dd/yyyy hh:tt"
    #num is either 0,1,2 where 0,1,2 refer to division of month or time 
    #form is either 0 or 1 and outputs month or time respectively
    #outputs mm if (0,0), dd if (0,1), yyyy if (0,2)
    #hh if (0,1), mm if (1,1)
    if form == 0:
        return date.split()[0].split("/")[num]
    else:
        return date.split()[1].split(":")[num]
    
#user input
Begin_date = raw_input("Begin Date (EX:05/26/2013 12:34):")
End_date = raw_input("End Date (EX:05/27/2013 22:34):")
    
mm1 = splitter(Begin_date,0,0)
dd1 = splitter(Begin_date,1,0)
yyyy1 = splitter(Begin_date,2,0)
hh1 = splitter(Begin_date,0,1)
tt1 = splitter(Begin_date,1,1)
mm2 = splitter(End_date,0,0)
dd2 = splitter(End_date,1,0)
yyyy2 = splitter(End_date,2,0)
hh2 = splitter(End_date,0,1)
tt2 = splitter(End_date,1,1)
#out = "month: %(mm)01s day: %(dd)01s year: %(year)04s" %{"mm": mm, "dd": dd, "year": yyyy}

req = ("http://www.cobbsheriff.org/inmate/JMS_Admit_Review.asp?BD=" + mm1 + "%2F" +
     dd1 + "%2F" + yyyy1 + "+" + hh1 + "%3A" + tt1 + "&CCLASS=&ED=" + mm2 + "%2F" +
     dd2 + "%2F" + yyyy2 + "+" + hh2 + "%3A" + tt2 + "&SK=")

#testing 01/27/2014 12:34 to 01/29/2014 13:10
#req = ("http://www.cobbsheriff.org/inmate/JMS_Admit_Review.asp?BD=01%2F27%2F2014+12%3A34&CCLASS=&ED=01%2F29%2F2014+13%3A10&SK=")

#Create a CookieJar object to hold the cookies
cj = cookielib.CookieJar()
#Create an opener to open pages using the http protocol and to process cookies.
opener = build_opener(HTTPCookieProcessor(cj), HTTPHandler())

#create a request object to be used to get the page.
req = Request(req)
f = opener.open(req)
f_out = open('Cobb County Unsorted.csv','w')
f_out.write('Last Name,First Name,Address,City,State,Zip,Charge,Charge Type,\n')

#see the first few lines of the page
html = f.read()

#Check out the cookies
for cookie in cj:
    cookieval = cookie.value
    cookiename = cookie.name

soup = BeautifulSoup(html,'html5lib')

for link in soup.findAll('a'):
    s = link.get('href')
    url = re.search(r'javascript:pop\("([^"]+)","(.*)"\);', s)
    if(url):
        opener = urllib2.build_opener()
        opener.addheaders.append(('Cookie', cookiename+'='+cookieval))
        f = opener.open("http://www.cobbsheriff.org/inmate/"+url.groups()[0])
        html = f.read()
        soup = BeautifulSoup(html)
        tables = soup.findAll('table')
        
        ### Personal Info ###
        table = tables[1]
        rows = table.findAll('tr')
        if (len(rows) >= 13):
            cols_name = rows[7].findAll('td')
            if (len(cols_name) >= 3):
                # name
                name = cols_name[0].text
                # splitting name on whitespace
                names = name.split(' ')
                firstname = names[1]
                lastname = names[0]
                
            cols_add = rows[11].findAll('td')
            if (len(cols_add) >= 4):
                # addresses
                address = cols_add[0].text
                address = address.replace(",","")
                city = cols_add[1].text
                state = cols_add[2].text
                postal = cols_add[3].text
                
        ### Charges ###
        for x in [9,10]:
            tab_test = tables[x]
            table_m = tab_test(text=re.compile('Misdemeanor'))
            table_f = tab_test(text=re.compile('Felony'))
            if (table_m) or (table_f):
                table_charge = tables[x]
                
        for row_charge in table_charge.findAll('tr'):
            cols_charge = row_charge.findAll('td')
            if (len(cols_charge) >= 6):
                charge_type_col = cols_charge[3]
                charge_type_m = charge_type_col(text=re.compile('Misdemeanor'))
                charge_type_f = charge_type_col(text=re.compile('Felony'))
                if (charge_type_m):
                    charge_type = 'M'
                    charge = cols_charge[2].text
                    charge = charge.replace(",", "")
                    f_out.write(lastname+','+firstname+','+address+','+city+','+state+','+ postal.strip() +','+charge+','+charge_type+'\n')
                elif (charge_type_f):
                    charge_type = 'F'
                    charge = cols_charge[2].text
                    charge = charge.replace(",", "")
                    f_out.write(lastname+','+firstname+','+address+','+city+','+state+','+ postal.strip()+','+charge+','+charge_type+'\n')

#finished
f_out.close()
