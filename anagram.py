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
            if j == i:
                # Skip the same word.
                continue
            # If the sorted words are equal then they are anagrams.
            if current_sorted_word == word_list_sorted[j]:
                # Append the non-sorted word.
                current_anagram.append(word_list[j])
        # If any anagrams was found.
        if len(current_anagram) > 0:
            current_anagram.insert(0, word_list[i])
            anagrams.append(current_anagram)
    return anagrams


def main():
    # TODO: after you have used one word you can safely remove it, it's impossible to be in
    #  multiple anagrams at the same time.
    # Read the eventyr.txt file.
    word_list = read_file("eventyr.txt")

    anagrams = find_anagram(word_list)
    for anagram in anagrams:
        print(", ".join(anagram))


if __name__ == '__main__':
    main()
