import json
import csv

def main():

    # load dictionary
    filename_read = "typeracer_text_dict.json"
    with open(filename_read, "r") as read_json:
        full_text_dict = json.load(read_json)

    # extract characters
    char_dict = extract_chars(full_text_dict)

    # write to csv
    write_to_csv(char_dict)

    return


def extract_chars(full_text_dict):
    # Iterates through all texts & extracts typed characters
    char_dict = {}
    
    # initialize case counters
    uppers = 0
    lowers = 0

    for key in full_text_dict:
        repetitions = full_text_dict[key][0]
        text = full_text_dict[key][1]

        for char in text:
            # ignore newline (\n) and carriage return (\r)
            # observed in keys: (3621065) (3621203)
            if (char == "\n") or (char == "\r"):
                continue

            # update case counters
            if ("A" <= char <= "Z"):
                uppers = uppers + (1*repetitions)
            elif ("a" <= char <= "z"):
                lowers = lowers + (1*repetitions)

            # add to dict as lowercase
            char = char.lower()
            if char in char_dict.keys():
                char_dict[char] = char_dict[char] + (1*repetitions)
            else:
                char_dict[char] = (1*repetitions)

    # save case counters
    count_str = "uppers:{}\nlowers:{}\n".format(uppers,lowers)
    filename_txt = "case_count.txt"
    with open(filename_txt, "w") as write_txt:
        write_txt.write(count_str)

    # save char_dict
    filename_json = "char_dict.json"
    with open(filename_json, "w") as write_json:
        json.dump(char_dict, write_json)
    
    return char_dict


def write_to_csv(char_dict):

    # connect to file
    filename_csv = "chars.csv"
    csv_file = open(filename_csv, "w", newline='')
    writer = csv.writer(csv_file)

    for key in char_dict.keys():
        writer.writerow([key, char_dict[key]])

    csv_file.close()
    return


if __name__ == "__main__":
    main()
