# ID Tag
# lex_auth_012693797166096384149

def find_leap_years(given_year):
    list_of_leap_years = []  # Create an empty list to store leap years
    
    # Loop until we have 15 leap years
    while len(list_of_leap_years) < 15:
        # Check if the current year is a leap year
        if (given_year % 4 == 0 and (given_year % 100 != 0 or given_year % 400 == 0)):
            list_of_leap_years.append(given_year)
        
        # Move to the next year
        given_year += 1
    
    return list_of_leap_years  # Return the final list

# Call the function with a starting year
list_of_leap_years = find_leap_years(2000)

# Print the result
print(list_of_leap_years)
