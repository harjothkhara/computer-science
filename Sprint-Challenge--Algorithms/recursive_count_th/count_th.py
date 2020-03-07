'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):
    count = 0
    # basecase - checking for "th" occurrences
    if word.startswith("th"):  # returns boolean
        count = 1

    # cases for recursive call
    if len(word) > 2:
        # removing first letter as we make our checks
        # returning count if "th" was found
        return count_th(word[1:len(word)] + count)
    else:
        return count
