# e) linear search


def LinearSearch(lys, element):
    for i in range(len(lys)):
        if lys[i] == element:
            return i
    return False


if __name__ == "__main__":
    print(LinearSearch([1, 2, 3, 4, 5, 2, 1], 2))
