import time


def read_file(path):
    """
    :param path: The path to the file.
    :return: A list of the words read from the file.
    """
    with open(path, encoding="utf-8") as f:
        file_content = f.read().strip().split("\n")
    return file_content


def sort_words(word_list):
    """
    :param word_list: A list of words.
    :return: The same length list and every word is still at the same index however the words
    are sorted alphabetically.
    """
    # TODO: A faster thing here would be to just count the number of chars. Instead of fully
    #  sorting it.
    return ["".join(sorted(word)) for word in word_list]


def simple_ord(char):
    if char == "æ":
        return 26
    if char == "ø":
        return 27
    if char == "å":
        return 28
    if char == "ó":
        return 29
    if char == "é":
        return 30
    return ord(char) - 97


def find_anagram_dictionary(word_list):
    """
    Takes about 0.00099945068359375 to run.
    This method is O(n). And works by going through the word_list once and sorting that word and
    checking if the dictionary already contains this sorted words as a key, in that case append
    the unsorted word in the list, otherwise create a new list with the unsorted word as the
    only value. In the end it iterates through the whole list and only keeps the anagrams with a
    list containing of more than 1 word.
    :param word_list: A list containing many words.
    :return: A list containing all the anagrams. Example: [["listen", "silent"]]
    """
    # A dictionary with the key being a sorted word and the value being all the unsorted words
    # with the same sorted words.
    anagrams = {}
    for word in word_list:
        # Get the sorted word.
        # sorted_word = "".join(sorted(word))
        sorted_word = [0] * 31
        for char in word:
            ord = simple_ord(char)
            sorted_word[ord] += 1
        # Check if this word has been seen already.
        sorted_word = str(sorted_word)
        if sorted_word in anagrams:
            # Already been seen then just append the word.
            anagrams[sorted_word].append(word)
        else:
            # Not been seen then we need to create a new list containing the new word.
            anagrams[sorted_word] = [word]
    # Only return the anagrams that have a list containing more than 1 word.
    return [anagram for anagram in anagrams.values() if (len(anagram) > 1)]


def find_anagram_naive(word_list):
    """
    This is a slow straightforward method. O(n^2).
    Takes about 0.12199807167053223 seconds.
    :param word_list: A list containing many words.
    :return: A list containing all the anagrams. Example: [["listen", "silent"]]
    """
    # Sort the file.
    word_list_sorted = sort_words(word_list)
    # This is a list containing all the sorted words that are already used.
    sorted_words_already_used = []
    # A list containing all the anagrams.
    anagrams = []
    for i in range(len(word_list)):
        current_sorted_word = word_list_sorted[i]
        if current_sorted_word in sorted_words_already_used:
            # If this word has already been checked then we can skip it.
            continue
        else:
            sorted_words_already_used.append(current_sorted_word)

        current_anagram = []
        for j in range(len(word_list)):
            # If the sorted words are equal then they are anagrams.
            if current_sorted_word == word_list_sorted[j]:
                # Append the non-sorted word.
                current_anagram.append(word_list[j])
        # Check if any anagrams was found. This always finds one (the same word) so we need to
        # check if we found more than 1.
        if len(current_anagram) > 1:
            anagrams.append(current_anagram)
    return anagrams


def main():
    # Read the eventyr.txt file.
    word_list = read_file("eventyr.txt")
    start = time.time()
    anagrams = find_anagram_dictionary(word_list)
    end = time.time()
    print("Finding the anagrams took", end - start, "seconds.")
    for anagram in anagrams:
        print(", ".join(anagram))


if __name__ == '__main__':
    main()
