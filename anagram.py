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


def main():
    # Read the eventyr.txt file.
    word_list = read_file("eventyr.txt")
    # Sort the file.
    word_list_sorted = sort_words(word_list)
    print(word_list_sorted)


if __name__ == '__main__':
    main()
