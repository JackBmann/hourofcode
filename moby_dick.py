import string

moby_dick = open("moby_dick.txt")

# initialize a list to contain words in Moby Dick
words = []

# populate the 'words' list with words in Moby Dick
for line in moby_dick:
    words_in_line = line.split()
    for word in words_in_line:
        # remove punctuation from word and add it to the list of words
        words.append(word.translate(None, string.punctuation))

# sort words alphabetically
words.sort()

# list to store distinct words in Moby Dick
words_without_dups = []
index = 0

while index < len(words):
    current_word = words[index]
    words_without_dups.append(current_word)
    # jump to the next different word
    while words[index] == current_word:
        index = index + 1
        # if our index reaches the end of the list, stop iteration
        if index >= len(words):
            break


# map to associate a canonicalized word to a list of its origins
anagram_map = {}

for word in words_without_dups:
    # sort the word
    sorted_word = ''.join(sorted(word))
    if sorted_word in anagram_map:
        anagram_map[sorted_word].append(word)
    else:
        anagram_map[sorted_word] = [word]


longest_anagram_key = ""
longest_anagram_key_len = 0;

for key in anagram_map:
    num_of_origins = len(anagram_map[key])
    if num_of_origins > longest_anagram_key_len:
        longest_anagram_key_len = num_of_origins
        longest_anagram_key = key

print "The longest anagram key is", longest_anagram_key
print "The words associated with the longest anagram key are:", anagram_map[longest_anagram_key]
