# Leetcode problem - word ladder

# Given two words (begin_word and end_word), and a dictionary's word list,
# return the shortest transformation sequence from begin_word to end_word, such that:
from util import Stack, Queue

# # Only one letter can be changed at a time.
# # Each transformed word must exist in the word list. Note that begin_word is not a transformed word.
# #
# # Return None if there is no such transformation sequence.
# # All words contain only lowercase alphabetic characters.
# # You may assume no duplicates in the word list.
# # You may assume begin_word and end_word are non-empty and are not the same.
# ​#
# 1. Translate the problem into graph terminology

# # Sample:
# # begin_word = "hit"
# # end_word = "cog"
# # return: ['hit', 'hot', 'cot', 'cog']
# ​#
# # begin_word = "sail"
# # end_word = "boat"
# # ['sail', 'bail', 'boil', 'boll', 'bolt', 'boat']
# ​
# # beginWord = "hungry"
# # endWord = "happy"
# # None


# 2: Build the Graph

# Load words from dictionary
f = open('words.txt', 'r')
# use a set instead of an array for words dictionary, for o(1) lookup instead of o(n)
word_set = set(f.read().lower().split("\n"))
# print(words)
f.close()

# to create words list: cp /usr/share/dict/words words.txt


def get_neighbors(word):  # 26n (26 letters in the alphabet) or o(n)
    '''
    Get all words that are one letter
    away from the given word
    '''
    # get same length words first
    results = []
    list_word = list(word)
    # Go through each letter in the word
    for i in range(len(list_word)):
        # Swap with each letter in the alphabet
        # 0(1) constant
        for letter in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']:
            # if resulting word is in the word_set, add to results
            # (Ignore if equal to the original word)
            temp_word = list_word.copy()
            temp_word[i] = letter
            joined_word = "".join(temp_word)
            if joined_word in word_set and joined_word != word:
                results.append(joined_word)
    return results

# get_neighbors("sail")

# bat

# cat, eat, fat, hat, lat, mat, oat, pat....
# bet, bit...
# bad, bae

# Create a counter that breaks if it goes higher than one and while loop through comparing

# Go through each word and build an adjacency list with each word one letter away

# Create an equality function


# goes through each letter in the alphabet and compare that to our given word. only changing w1
# def words_are_neighbors(w1, w2):  # 1
#     '''
#     return True if words are one letter apart
#     False otherwise
#     '''
#     list_word = list(w1)
#     # Go through each letter in the word
#     for i in range(len(list_word)):
#         # Swap with each letter in the alphabet
#         for letter in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']:
#             # Check if that equals given word
#             temp_word = list_word.copy()
#             temp_word[i] = letter
#             if "".join(temp_word) == w2:
#                 return True
#     return False
# # bat e,g w1
# # aat
# # cat ✅ matches our w2
# # words_are_neighbors("abc", "abd")
# # delete a letter at each place, and if after deleting one letter we get two matching strings on the left and right side, that means we have a match.


# def words_are_neighbors(w1, w2):  # 2
#     print(f"comparing {w1} - {w2}")
#     if len(w1) != len(w2):
#         return False
#     for i in range(len(w1)):
#         # print(f"{w1[:i]}, {w2[:i]}, {w1[i+1:]}, {w2[i+1:]}")
#         if w1[:i] == w2[:i] and w1[i+1:] == w2[i+1:]:
#             return True
#     return False

#  words_are_neighbors("abc", "abd")

# def words_are_neighbors(word1, word2):  # 3 - cleaner
#     for i in range(len(word1)):
#         list_word1 = list(word1)
#         list_word2 = list(word2)
#         list_word1.pop(i)
#         list_word2.pop(i)
#         if list_word1 == list_word2:
#             return True


# words_are_neighbors("abc", "abd")

# # build an adjacency list
# neighbors = {}
# # a word is a neighbor if every character in each word matches except for one
# # go through each word
# for word in word_set:
#     # add that word to the dictionary
#     neighbors[word] = set()
#     # for each word we need to go through each potential neighbor
#     for potential_neighbor in word_set:
#         # add to neighbors if they match
#         if words_are_neighbors(word, potential_neighbor):
#             neighbors[word].add(potential_neighbor)


# def get_neighbors(word):
#     return neighbors[word]

# 3. Traverse the graph (BFS)
def word_ladder(begin_word, end_word):
    """
    Return a list containing the shortest path from
    starting_vertex to destination_vertex in
    breath-first order.
    """
    # Create a queue
    q = Queue()
    # Enqueue a path to starting word
    q.enqueue([begin_word])
    # Create a visited set
    visited = set()
    # While queue is not empty:
    while q.size() > 0:
        # Dequeue path
        path = q.dequeue()
        # Grab the last word from the path
        w = path[-1]
        # Check if its our target word
        if w == end_word:
            # If so, return path
            return path
        # Check if it's been visited
        if w not in visited:
            # If not, mark as visited
            visited.add(w)
            # Enqueue path to each neighboring word
            for neighbor in get_neighbors(w):
                # Make a copy of the path
                path_copy = path.copy()
                # Add neighbor to the new path
                path_copy.append(neighbor)
                # Enqueue the copy of the path
                q.enqueue(path_copy)


print("HERE")
print(word_ladder("sail", "boat"))
print("END")
