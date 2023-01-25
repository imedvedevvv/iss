import sys
import os
import re
import json


def inverted_index(text, index_dict, filename):
    words = re.findall(r'(?:(?<=[^a-zA-Z])|(?<=^))[a-zA-Z]+(?:(?=[^a-zA-Z])|(?=$))', text)
    for word in words:
        normalized_word = word.lower()
        if normalized_word not in index_dict:
            index_dict[normalized_word] = []

        if filename not in index_dict[normalized_word]:
            index_dict[normalized_word].append(filename)

    return


if __name__ == "__main__":
    if (len(sys.argv[1:]) > 1):
        raise "Unexpected arguments!"

    DOCS_DIR = './docs'
    OUT_FILENAME = 'inverted_index.json'
    words_inverted_index_dict = {}
    for filename in os.listdir(DOCS_DIR):
        path = os.path.join(DOCS_DIR, filename)
        f = open(path, 'r')
        inverted_index(f.read(), words_inverted_index_dict, filename)

    output = open(OUT_FILENAME, 'w')
    output.write(json.dumps(words_inverted_index_dict, indent=4))
