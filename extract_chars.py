import json
import csv

def main():

    # load dictionary
    with open("typeracer_text_dict.json", "r") as read_json:
        full_text_dict = json.load(read_json)

    # extract characters
    char_dict = extract_chars(full_text_dict)

    # write to csv
    write_to_csv(char_dict)

    return


def extract_chars(full_text_dict):
    # Iterates through all texts & extracts typed characters
    char_dict = {}
    
    # initialize extra counters
    uppers = 0
    lowers = 0
    numbers = 0
    specials = 0
    total_chars = 0

    for key in full_text_dict:
        repetitions = full_text_dict[key][0]
        text = full_text_dict[key][1]
        total_chars = total_chars + len(text)

        for char in text:
            # ignore newline (\n) and carriage return (\r)
            # observed in keys: (3621065) (3621203)
            if (char == "\n") or (char == "\r"):
                continue

            # update extra counters
            if ("A" <= char <= "Z"):
                uppers = uppers + (1*repetitions)
            elif ("a" <= char <= "z"):
                lowers = lowers + (1*repetitions)
            elif ("0" <= char <= "9"):
                numbers = numbers + (1*repetitions)
            elif (char != " "):
                specials = specials + (1*repetitions)

            # add to dict as lowercase
            char = char.lower()
            if char in char_dict.keys():
                char_dict[char] = char_dict[char] + (1*repetitions)
            else:
                char_dict[char] = (1*repetitions)

    # save the extra counters
    count_str = "total:{}\nuppers:{}\nlowers:{}\nnumbers:{}\nspecials:{}"\
        .format(total_chars,uppers,lowers,numbers,specials)
    with open("simple_char_count.txt", "w") as write_txt:
        write_txt.write(count_str)

    # save char_dict
    with open("char_dict.json", "w") as write_json:
        json.dump(char_dict, write_json)
    
    return char_dict


def write_to_csv(char_dict):

    csv_file = open("extracted_chars.csv", "w", newline='')
    writer = csv.writer(csv_file)

    for key in char_dict.keys():
        writer.writerow([key, char_dict[key]])

    csv_file.close()
    return


if __name__ == "__main__":
    main()
