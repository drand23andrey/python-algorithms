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

def sortHoar(lst):
    """ сортировка Хоара (быстрая) """
    if len(lst) < 2:
        return lst
    check = lst[0]
    mid = []
    low = []
    high = []
    for n in lst:
        if n == check:
            mid.append(n)
        elif n < check:
            low.append(n)
        else:
            high.append(n)
    
    return sortHoar(low) + mid + sortHoar(high)

def sortMerge(lst):
    """ сортировка методом слияния """
    L = len(lst)
    if L <= 1:
        return lst
    left, right = sortMerge(lst[:round(L/2)]), sortMerge(lst[round(L/2):])
    lst = []

    while True:
        if not left and not right:
            break
        elif not left:
            lst = lst + right
            right = []
            continue
        elif not right:
            lst = lst + left
            left = []
            continue
        elif left[0] == right[0]:
            lst.append(left.pop(0))
            lst.append(right.pop(0))
            continue
        elif left[0] < right[0]:
            lst.append(left.pop(0))
            continue
        elif left[0] > right[0]:
            lst.append(right.pop(0))
            continue
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
    testSort(sortHoar)
    testSort(sortMerge)