#lex_auth_01269361601342668881
def calculate_total_ticket_cost(no_of_adults, no_of_children):
    adult=float(37550)
    child=adult/3
    total_ticket_cost= adult*no_of_adults + child*no_of_children
    aftertax = total_ticket_cost + (total_ticket_cost * 0.07)
    finalwithdiscount = aftertax - (aftertax * 0.10)

    #Write your logic here

    return finalwithdiscount


#Provide different values for no_of_adults, no_of_children and test your program
amt=calculate_total_ticket_cost(5,2)
print("Total Ticket Cost:",amt)

# The function calculate_total_ticket_cost calculates the total cost of tickets for adults and children.
# Adult ticket price is set to 37550.
# Child ticket price is one third of the adult ticket price.
# The total ticket cost is calculated by multiplying the number of adults and children by their respective ticket prices.
# A 7% tax is added to the total ticket cost.
# A 10% discount is applied to the amount after tax.
# The final ticket cost after tax and discount is returned.

# The function is tested with 5 adults and 2 children.
# The result is printed as the total ticket cost.