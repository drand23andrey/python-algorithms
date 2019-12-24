def matryoshka(n):
    """строим матрешку"""
    if n == 1:
        # крайний случай
        print('Самая маленькая матрешка n = ', n)
    else:
        # рекуррентный случай
        print('Верх матрешки n = ', n)
        matryoshka(n-1)
        print('Низ матрешки n = ', n)

def factorial(n):
    """считаем факториал"""
    assert n >= 0, 'Факториал отрицательный'
    if n < 2:
        return 1
    return n * factorial(n-1)

def gcd(a, b):
    """ наибольший общий делитель """
    if a==b: 
        return a
    elif a > b:
        return gcd(a-b, b)
    else:
        return gcd(a, b-a)
    # TODO сделать через %

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

# TODO сделать хайноские башни

# TODO сделать возведение в степень (с делением пополам)

if __name__ == "__main__":
    matryoshka(5)
    print(factorial(5))
    print(gcd(6, 5))
    
    genNum(1) # 1
    genNum(2) # 12 21
    genNum(3) # 123 312 231 132 213 321
