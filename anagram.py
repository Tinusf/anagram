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


def find_anagram(word_list):
    """
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
    # TODO: after you have used one word you can safely remove it, it's impossible to be in
    #  multiple anagrams at the same time.
    # Read the eventyr.txt file.
    word_list = read_file("eventyr.txt")
    start = time.time()
    anagrams = find_anagram(word_list)
    end = time.time()
    print(end - start)  # Takes about 0.12199807167053223.
    for anagram in anagrams:
        print(", ".join(anagram))


if __name__ == '__main__':
    main()
