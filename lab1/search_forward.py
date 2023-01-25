import sys
import json


def search_forward(index, keyword):
    result = []
    for filename in index:
        if keyword in index[filename]:
            result.append(filename)
    return result


if __name__ == "__main__":
    if (len(sys.argv) < 2):
        raise "No arguments provided!"

    try: 
        index_file = open('./forward_index.json', 'r')
    except:
        raise "Index not found!"

    index = json.loads(index_file.read())
    for keyword in sys.argv[1:]:
        result = search_forward(index, keyword)
        result_str = ', '.join(result)
        print(f'{keyword}: {result_str}')
