# Euler Problem #19: Counting Sundays
# http://projecteuler.net/problem=19
# Q: How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
# A: 171

# 1 Jan 1900 was a Monday.
# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
    
# Move forward to Jan 1, 1901. 1900 is not a leap year; 365 days
# 365 % 7 = 1
# Jan 1, 1901 is on Tuesday ;31 % 7 = 3; jump forward days mod 7 total days
# Feb 1, 1901 is on Friday
# Mar 1, 1901 is on Friday
# Apr 1, 1901 is on Monday
# May 1, 1901 is on Wednesday
# June 1, 1901 is on Saturday
# July 1, 1901 is on Monday
# August 1, 1901 is on Thursday
# September 1, 1901 is on Sunday
# Oct 1 , 1901 is on Tuesday
# Nov 1, 1901 is on Friday
# Dec 1, 1901 is on Sunday

# Let Sunday = 0, Monday = 1... Friday = 6
# Store first of month days in list with first element being Jan, last element being december
# i.e month_day[0] is the day of the week of January 1

# Initialize
count = 2
month_day = [2,5,5,1,3,6,1,4,0,2,5,0]
leap = False
leap_past = False

# Iterate over all years, check if the first of each month lies on sunday. increment counter if yes.
# move forward first of month by 1 day; 
# for Jan, Feb, move forward 2 days if leap year was the year prior.
# for rest of months, move forwards 2 days if leap year is current year.

for year in range(1902,2001):
    leap_past = leap
    if year % 400 == 0:
        leap = True
    elif year % 100 == 0:
        leap = False
    elif year % 4 == 0:
        leap = True
    else:
        leap = False
    for m in range(12): # ((m == 0 or m == 1) and leap_past) or leap
        if (m == 0 or m == 1) and leap_past: #if was a leap year last year for Jan or Feb
            month_day[m] = (month_day[m] + 2) % 7
        elif m >= 1 and leap: # or leap year for this year for all other months
            month_day[m] = (month_day[m] + 2) % 7
        else:
            month_day[m] = (month_day[m] + 1) % 7
        if month_day[m] == 0: # if falls on sunday
            count += 1
            #print year
            #print m
print count
        

