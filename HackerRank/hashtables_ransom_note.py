from collections import Counter
# Harold is a kidnapper who wrote a ransom note, but now he is worried it will be traced back to him through his handwriting. He found a magazine and wants to know if he can cut out whole words from it and use them to create an untraceable replica of his ransom note. The words in his note are case-sensitive and he must use only whole words available in the magazine. He cannot use substrings or concatenation to create the words he needs.

# Given the words in the magazine and the words in the ransom note, print Yes if he can replicate his ransom note exactly using whole words from the magazine; otherwise, print No.

# For example, the note is "Attack at dawn". The magazine contains only "attack at dawn". The magazine has all the right words, but there's a case mismatch. The answer is .

# https://www.hackerrank.com/challenges/ctci-ransom-note/problem?h_l=interview&isFullScreen=false&playlist_slugs%5B%5D%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D%5B%5D=dictionaries-hashmaps

# Complete the checkMagazine function below. - naive solution o(n**2). basic tests pass but not all the extended tests
def checkMagazine(magazine, note):
    word_n = note
    word_m = magazine
    # a set can contain no duplicate values
    match = set()
    # loop through each word in note
    for i in range(len(word_n)):
      # for each word in note see if the same word exists in the magazine
        for j in range(len(word_m)):
          # if it does, then add it to the set (can't use the same word twice from the magazine 
          # that's why added to set(), no duplicates, unordered
            if (word_n[i] == word_m[j]):
                match.add(word_m[j])
    # once the check between the magazine words and note is complete
    # check whether the words we found from the magazine are equal to words in notes
    if len(word_n) == len(match):
        print("Yes")
    else:
        print("No")

# optimized version using Counter from Python collection libaray - passes all tests!
 #Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    # using Counter(keep track of hashtable objects. elements are stored as dict keys and their counts are stored as dict values) to keep track of word occcurances in magazine and ransom note. keep track of the numnber of times the same string has been hashed, storing the string as the key and the count as the value.
    mag = Counter(magazine) 
    # e.g Counter({'give': 1, 'me': 1, 'one': 1, 'grand': 1, 'today': 1, 'night': 1})
    note = Counter(note) 
    # Counter({'give': 1, 'one': 1, 'grand': 1, 'today': 1})
    
    # 
    if note - mag == {}:
        print("Yes")
    else:
        print("No")