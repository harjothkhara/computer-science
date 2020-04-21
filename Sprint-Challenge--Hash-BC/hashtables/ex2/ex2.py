#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source # starting airport
        self.destination = destination # next airport

# We can hash each ticket such that the starting location is the key and the destination is the value.

def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    """
    YOUR CODE HERE
    since we need all the tickets, insert all the tickets to a HT
    key:value
    source: destination
    if source is None, first trip, append the destination to results
    while destination is not None, append the destination to the results
    """
    flight_order = []
    # HT insertion
    # since we need all the tickets, insert all the tickets to a HT
    for ticket in tickets:
        hash_table_insert(hashtable, ticket.source, ticket.destination)
    # Finding first destination
    # retrieving the destination value associated with the "None" key at source.
    # the ticket for your first flight has a destination with a source of NONE
    if hash_table_retrieve(hashtable, "NONE"):
        # append key with source = "None" to flight_order array
        flight_order.append(hash_table_retrieve(hashtable, "NONE"))
    # flight_order = [PDX]

    # using HT to search for next destination
                       # 3
    for i in range(0, length - 2): # i=0 - exclude start and end
        flight_order.append(hash_table_retrieve(
            # pulls last destination out from the array (cleanup) and use as key for value (next destination) retrieval
            hashtable, flight_order[-1:][0]))
            # flight_order = [PDX]
            # use PDX as key for next destination retrieval from HT
            # [PDX, DCA]
            # pull and use PDX as key for next destination retrieval from HT

    return flight_order


ticket_1 = Ticket("NONE", "PDX")
ticket_2 = Ticket("PDX", "DCA")
ticket_3 = Ticket("DCA", "NONE")

tickets = [ticket_1, ticket_2, ticket_3]

result = reconstruct_trip(tickets, 3)
# ['PDX', 'DCA']
print(result)
