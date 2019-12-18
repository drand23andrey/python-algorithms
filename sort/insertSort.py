def insertSort(A):
    for i in range(0, len(A)):
        if not i:
            continue
        while A[i] < A[i - 1] and i > 0:
            A[i], A[i - 1] = A[i - 1], A[i]
            i -= 1
    return A

def testInsertSort():
    x = insertSort(A = [2, 4, 5, 1, 3])
    y = list(range(1, 6))
    if x == y:
        print('testInsertSort - OK')
        return 1
    print('testInsertSort - Error')
    return -1

testInsertSort()
print('All test are OK')