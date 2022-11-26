import csv
import json
import pandas as pd

def main():

    word_list = get_words()
    len_dict = dict()

    for word in word_list:
        char_set = set(word)
        word_len = len(word)
        
        for char in char_set:
            if char.isalpha():     # only alphabetical
                if char in len_dict.keys():
                    len_dict[char].append(word_len)
                else:
                    len_dict[char] = [word_len]
            
    save_results(len_dict)

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

def save_results(len_dict):
    destination = "./data/letter-wordlength.csv"
    
    # pandas dataframe to format & export easily
    df = pd.DataFrame(dict([ (k,pd.Series(v)) for k,v in len_dict.items() ]))
    df.to_csv(destination, index=False)

    return


if __name__ == "__main__":
    main()
