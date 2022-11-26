import csv

def main():
    # Finds words that can be typed with one hand (one side of keyboard)
    word_list = get_words()

    chars_left = "qwertasdfgzxcvb"
    chars_right = "yuiophjkl'nm"

    set_left = set()
    set_right = set()

    for word in word_list:
        for char in word:
            if (word in set_left) and (word in set_right):
                break   # goto next word
            if char in chars_left:
                set_left.add(word)
            elif char in chars_right:
                set_right.add(word)

    # set difference (or sym diff) yields one-handed words
    words_left = set_left.difference(set_right)
    words_right = set_right.difference(set_left)

    # save results
    save_results(words_left, words_right)

    return


def get_words():
    # read the words from words.csv into a list
    word_list = []

    filename_words = "./data/words.csv"
    with open(filename_words, "r") as read_csv:
        reader = csv.reader(read_csv, delimiter=',')
        for row in reader:
            word_list.append(row[0])

    return word_list


def save_results(words_left, words_right):
    # saves results to separate .txt files
    file_left = "./data/left_handed_words.txt"
    file_right = "./data/right_handed_words.txt"
    
    with open(file_left, "w") as file_left:
        file_left.writelines("\n".join(words_left))
    with open(file_right, "w") as file_right:
        file_right.writelines("\n".join(words_right))

    return



if __name__ == "__main__":
    main()