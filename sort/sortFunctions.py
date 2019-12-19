def insertSort(lst):
    """ сортировка вставками O(N2) """
    for i in range(1, len(lst)):
        while lst[i] < lst[i - 1] and i > 0:
            lst[i], lst[i - 1] = lst[i - 1], lst[i]
            i -= 1
    return lst

def choiseSort(lst):
    """ сортировка выбором O(N2) """
    for i in range(0, len(lst)):
        min = i
        for j in range(i, len(lst)):
            if lst[j] < lst[min]:
                min = j
        lst[i], lst[min] = lst[min], lst[i]
    return lst

def bobbleSort(lst):
    """ сортировка методом пузырька O(N2) """
    for i in range(0, len(lst)):
        for j in range(0, len(lst) - i - 1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst


def testSort(someSortFunction):
    print("Now test: " + someSortFunction.__doc__ + ' ', end='')
    x = someSortFunction([2, 4, 5, 1, 3])
    y = list(range(1, 6))
    print("OK" if x == y else "Fail")


if __name__ == "__main__":    
    testSort(insertSort)
    testSort(choiseSort)
    testSort(bobbleSort)