import sys
import os
import re
import json


def forward_index(text):
    words_forward_index = []
    words = re.findall(r'(?:(?<=[^a-zA-Z])|(?<=^))[a-zA-Z]+(?:(?=[^a-zA-Z])|(?=$))', text)
    for word in words:
        normalized_word = word.lower()
        if normalized_word not in words_forward_index:
            words_forward_index.append(normalized_word)

    words_forward_index.sort()

    return words_forward_index


if __name__ == "__main__":
    if (len(sys.argv) > 1):
        raise "Unexpected arguments!"

    DOCS_DIR = './docs'
    OUT_FILENAME = 'forward_index.json'
    words_forward_index_dict = {}
    for filename in os.listdir(DOCS_DIR):
        path = os.path.join(DOCS_DIR, filename)
        f = open(path, 'r')
        words_forward_index_dict[filename] = forward_index(f.read())

    output = open(OUT_FILENAME, 'w')
    output.write(json.dumps(words_forward_index_dict, indent=4))
