import sys


def common(list1, list2):
    result = []
    for item in list1:
        if item not in result and item in list2:
            result.append(item)

    return result


if __name__ == "__main__":
    args = sys.argv[1:]
    if len(args) != 2:
        raise "2 comma-separated lists should be provided as arguments"

    list1 = args[0].split(',')
    list2 = args[1].split(',')
    print('Common elements: ' + ', '.join(common(list1, list2)))
