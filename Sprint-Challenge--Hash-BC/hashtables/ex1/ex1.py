#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    # initialized and set to capacity 16
    ht = HashTable(16)
    # for the first weight in the range from 0 to length
    for weight_1 in range(0, length):  # index
        # insert hashtable, [weight key], and weight value
        hash_table_insert(ht, weights[weight_1], weight_1)
    # for the second weight in the range from 0 to length
    for weight_2 in range(0, length):
        # subtract [weight value] from limit and assign result to matching_weight
        matching_weight = limit - weights[weight_2]
        # retrieve the matching wight from the hash table and assign to found_weight
        found_weight = hash_table_retrieve(ht, matching_weight)
        # if we found a weight ...
        if found_weight:
            # return the found weight and its partner_weight_2
            return (found_weight, weight_2)
    # return None (means no matching weight was found)
    return None


test_weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
matching_weights = get_indices_of_item_weights(test_weights, 10, 11)
# should return 9, 0 (10 + 1 = 11)
print(matching_weights)


# def print_answer(answer):
#     if answer is not None:
#         print(str(answer[0] + " " + answer[1]))
#     else:
#         print("None")
