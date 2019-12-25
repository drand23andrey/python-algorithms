def leftBound(lst, x):
    """ поиск левой границы поиска """
    left_border = -1
    right_border = len(lst)
    while right_border - left_border > 1:
        middle = round((left_border + right_border) / 2)
        if x > lst[middle]:
            left_border = middle
        else:
            right_border = middle
    return left_border

def rightBound(lst, x):
    """ поиск правой границы """
    left_border = -1
    right_border = len(lst)
    while right_border - left_border > 1:
        middle = round((left_border + right_border) / 2)
        if x >= lst[middle]:
            left_border = middle
        else:
            right_border = middle
    return right_border

def binFinderFirst(lst, x):
    if rightBound(lst, x) - leftBound(lst, x) <= 1:
        return -1
    else:
        return leftBound(lst, x) + 1

if __name__ == "__main__":
    print(binFinderFirst([1,2,3,3,4,5,6,8,9,9,10], 2)) # 1
    print(binFinderFirst([1,2,3,3,4,5,6,8,9,9,10], 3)) # 2
    print(binFinderFirst([1,2,3,3,4,5,6,8,9,9,10], 7)) # -1
    print(binFinderFirst([1,2,3,3,4,5,6,8,9,9,10], 1)) # 0
    print(binFinderFirst([1,2,3,3,4,5,6,8,9,9,10], 10)) # 10
    print(binFinderFirst([1,2,3,3,4,5,6,8,9,9,10], 0)) # -1
    print(binFinderFirst([1,2,3,3,4,5,6,8,9,9,10], 11)) # -1