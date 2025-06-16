def generate_tickets(airline, nub_passengers, source, destination):
    # Extract first 3 letters of source, airline, and destination, and convert to uppercase
    src_code = source[:3].upper()
    aln = airline[:3].upper()
    dst = destination[:3].upper()

    ticket_list = []
    # Generate ticket numbers for each passenger
    for i in range(nub_passengers):
        # Format: AIRLINE:SRC:DST:TICKET_NUMBER (starting from 101)
        ticket_number = f"{aln}:{src_code}:{dst}:{101+i}"
        ticket_list.append(ticket_number)

    # Return the last 5 tickets generated
    return ticket_list[-5:]

# Generate tickets for 32 passengers from Delhi to Pune on Air India
ticket = generate_tickets("airindia", 32, 'delhi', 'pune')
print(ticket)
