import sys
import json


def search_inverted(index, keyword):
    result = index[keyword] if keyword in index else []
    return result


if __name__ == "__main__":
    if (len(sys.argv) < 2):
        raise "No arguments provided!"

    try:
        index_file = open('./inverted_index.json', 'r')
    except:
        raise "Index not found!"

    index = json.loads(index_file.read())
    for keyword in sys.argv[1:]:
        result = search_inverted(keyword)
        result_str = ', '.join(result)
        print(f'{keyword}: {result_str}')
