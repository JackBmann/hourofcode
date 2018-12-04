import string

def get_words():
    # initialize a list to contain words in Moby Dick
    words = []
    moby_dick = open("MobyDick.txt")

    # populate the 'words' list with words in Moby Dick
    for word in moby_dick.read().split():
        # remove punctuation from word and add it to the list of words
        words.append(word.translate(None, string.punctuation).lower())
        # print words[-1]
    return words

def build_word_list_without_duplicates(original_list):
    # list to store distinct words in Moby Dick
    words_without_dups = []

    index = 0

    while index < len(original_list):
        current_word = original_list[index]
        words_without_dups.append(current_word)
        # jump to the next different word
        while original_list[index] == current_word:
            index = index + 1
            # if our index reaches the end of the list, stop iteration
            if index >= len(original_list):
                break
    return words_without_dups

def build_dictionary(word_list):
    # map to associate a canonicalized word to a list of its origins
    anagram_map = {}
    for word in word_list:
        # sort the word
        sorted_word = ''.join(sorted(word))
        if sorted_word in anagram_map:
            anagram_map[sorted_word].append(word)
        else:
            anagram_map[sorted_word] = [word]
    return anagram_map

def get_largest_anagram_set_key(dict):
    largest_anagram_key = ""
    largest_anagram_key_len = 0
    for key in dict:
        num_of_origins = len(dict[key])
        if num_of_origins > largest_anagram_key_len:
            longest_anagram_key_len = num_of_origins
            largest_anagram_key = key
    return (largest_anagram_key, largest_anagram_key_len)

def get_longest_anagrams(dict):
    longest_anagram_key = ""
    longest_anagram_key_len = 0
    for key in dict:
        if len(dict[key]) > 3 and len(key) > longest_anagram_key_len:
            longest_anagram_key_len = len(key)
            longest_anagram_key = key
    return (longest_anagram_key, dict[longest_anagram_key])


words = get_words()
# sort words alphabetically
words.sort()
words_without_dups = build_word_list_without_duplicates(words)
anagram_map = build_dictionary(words_without_dups)

longest_key, longest_key_len = get_largest_anagram_set_key(anagram_map)

print "The longest key (" + longest_key + ") has", longest_key_len, "words"
print "The words associated with the most frequent anagram key are:", anagram_map[longest_key]
print "The longest anagrams are:", get_longest_anagrams(anagram_map), 
