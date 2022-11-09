import json
import re
import csv

def main():
    # load dictionary
    filename_read = "typeracer_text_dict.json"
    with open(filename_read, "r") as read_json:
        full_text_dict = json.load(read_json)

    # extract words
    word_dict = extract_words(full_text_dict)

    # write to csv
    write_to_csv(word_dict)

    return


def extract_words(full_text_dict):
    # regex to split text into words. Add words to dict
    word_dict = {}

    for key in full_text_dict.keys():
        repetitions = full_text_dict[key][0]
        text = full_text_dict[key][1]

        split_text = re.findall(r"[\w']+", text)

        for word in split_text:
            # normalize to lower case
            word = word.lower()

            # light word cleaning
            if word == "'":
                continue
            if word[0] == "'":
                word = word[1:]
            if word[-1] == "'":
                word = word[:-1]

            # add to dictionary
            if word in word_dict.keys():
                word_dict[word] = word_dict[word] + (1*repetitions)
            else:
                word_dict[word] = (1*repetitions)

    return word_dict


def write_to_csv(word_dict):

    # connect to file
    filename_csv = "words.csv"
    csv_file = open(filename_csv, "w", newline='')
    writer = csv.writer(csv_file)

    for key in word_dict.keys():
        writer.writerow([key, word_dict[key]])

    csv_file.close()
    return



if __name__ == "__main__":
    main()