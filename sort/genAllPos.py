def genNum(n, m=-1, lst=[]):
    """
    генератор случайных комбинаций с цифрами от 1 до N
    """
    if m == 0:
        print(lst)
        return
    elif m == -1:
        m = n
    for number in range(1, n+1):
        if number in lst:
            continue
        lst.append(number)
        genNum(n, m-1, lst)
        lst.pop()
    return

if __name__ == "__main__":
    genNum(1) # 1
    genNum(2) # 12 21
    genNum(3) # 123 312 231 132 213 321