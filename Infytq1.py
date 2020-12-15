#Write a Python program to generate the next 15 leap years starting from a given year. Populate the leap years into a list and display the list.


def find_leap_years(given_year):

    # Write your logic here
        for i in range(1,4):
            if(given_year%4!=0):
                given_year=given_year+1
            else:
                break
            
        list_of_leap_years=[given_year,given_year+4,given_year+8,given_year+12,given_year+16,given_year+20,given_year+24,given_year+28,given_year+32,given_year+36,given_year+40,given_year+44,given_year+48,given_year+52,given_year+56]

        return list_of_leap_years

list_of_leap_years=find_leap_years(2001)
print(list_of_leap_years)
