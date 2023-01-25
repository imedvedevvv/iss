import sys
import os
import json
import string
import re
from common_elements import common


def create_index(filenames, index, file_titles):
    for filename in filenames:
        f = open(filename, 'r')
        text = f.read()
        f.close()
        title = re.findall(r'^.*(?=[\n])|(?=$)', text)[0]
        file_titles[filename] = title
        words = re.findall(r'(?:(?<=[ \n])|(?<=^))[^ \n]+(?:(?=[ \n])|(?=$))', text)
        for word in words:
            normalized_word = word.lower().strip(string.punctuation)
            if not normalized_word:
                continue

            if normalized_word not in index:
                index[normalized_word] = []

            if filename not in index[normalized_word]:
                index[normalized_word].append(filename)

    return


def search(index, query):
    terms = re.findall(r'(?:(?<=[ \n])|(?<=^))[^ \n]+(?:(?=[ \n])|(?=$))', query)
    result = []

    for term in terms:
        if term not in index:
            return []

        if len(result) == 0:
            result = index[term]
            continue

        result = common(result, index[term])
            

    return result

if __name__ == "__main__":
    args = sys.argv[1:]
    
    if len(args) < 1:
        raise "Arguments expected!"
    
    if len(args) > 2 or (len(args) == 2 and args[1] != '-s'):
        raise "Unexpected arguments!"

    DOCS_DIR = sys.argv[1]
    INDEX_FILENAME = 'inverted_index.json'
    TITLES_FILENAME = 'titles_dict.json'
    index = {}
    file_titles = {}
    filenames = [os.path.join(DOCS_DIR, filename) for filename in os.listdir(DOCS_DIR)]
    create_index(filenames, index, file_titles)

    index_output = open(INDEX_FILENAME, 'w')
    index_output.write(json.dumps(index, indent=4))
    index_output.close()

    titles_output = open(TITLES_FILENAME, 'w')
    titles_output.write(json.dumps(file_titles, indent=4))
    titles_output.close()

    if len(args) == 2 and args[1] == '-s':
        while True:
            query = input("Please enter the search query:\n")
            if not query:
                break
            print(search(index, query))
