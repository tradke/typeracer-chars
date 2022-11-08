#----------------------------------------------------------------------------
# Author: Tyler Radke
# Date: Nov 7, 2022
# ---------------------------------------------------------------------------
""" Purpose: scrape the full typeracer race text for acollection of 
    text_ids. Saves (and reloads) data as a .json

    Dictionary format: {text_id:[count, text]}

    1) Loads old_dict from .json (if exists)
    2) Create new_dict from .csv
    3) get texts from old_dict or web scraping
    4) save new_dict as a .json
"""

import json
import csv
import requests
from bs4 import BeautifulSoup
import time


def main():
    # define filenames
    filename_json = "typeracer_text_dict.json"
    filename_csv = "races.csv"

    # Try to load an existing dictionary
    try:
        with open(filename_json, "r") as read_json:
            old_dict = json.load(read_json)
    except FileNotFoundError:
        old_dict = {}

    # Create new_dict from .csv
    new_dict = read_csv(filename_csv)

    # get texts from old_dict or web scraping 
    get_texts(new_dict, old_dict)

    # save dict as .json
    with open("typeracer_text_dict.json", "w") as write_json:
        json.dump(new_dict, write_json)

    return


def read_csv(filename_csv):
    # Create new_dict from .csv

    new_dict = {}

    with open(filename_csv, "r") as read_csv:
        reader = csv.reader(read_csv)
        next(reader)    # skip first line (header)
        for row in reader:
            text_id = row[0]
            if text_id in new_dict.keys():
                count = new_dict[text_id][0] + 1
            else:
                count = 1
            new_dict[text_id] = [count, ""]

    return new_dict


def get_texts(new_dict, old_dict):
    # gets full_text from old_dict or website

    url_template = "https://typeracerdata.com/text?id="

    # initialize progress estimator
    keys_todo = len(new_dict.keys()) - len(old_dict.keys())
    time_start = time.time()
    i = 0

    for key in new_dict.keys():
        if key in old_dict.keys():
            full_text = old_dict[key][1]
        else:
            # load webpage
            url = url_template + key
            webpage = requests.get(url)

            # beautifulsoup to extract text. Found in first <p>
            soup = BeautifulSoup(webpage.text, "html.parser")
            full_text = soup.p.get_text()[2:]

            # progress estimator
            i = i + 1
            if (i%100 == 0):
                print("({} / {}) ".format(i, keys_todo), end="")
                print("Time elapsed: {:.1f} min".format((time.time()-time_start)/60))

        # store full_text in dict
        new_dict[key] = [new_dict[key][0], full_text]


    return


if __name__ == "__main__":
    main()