'''динамическое программирование'''

def fib_req(n):
    if n <= 1:
        return n
    return fib_req(n-1) + fib_req(n-2)

def fib_dyn(n):
    lst = [0, 1]
    if n <= 1:
        return lst[n]
    for n in range(0, n-1):
        lst[0], lst[1] = lst[1], lst[0] + lst[1]
    return lst[1]

if __name__ == "__main__":
    print(fib_req(0))   # 0
    print(fib_req(1))   # 1
    print(fib_req(2))   # 1
    print(fib_req(3))   # 2
    print(fib_req(4))   # 3
    print(fib_req(5))   # 5
    print(fib_req(6))   # 8

    print('')

    print(fib_dyn(0))   # 0
    print(fib_dyn(1))   # 1
    print(fib_dyn(2))   # 1
    print(fib_dyn(3))   # 2
    print(fib_dyn(4))   # 3
    print(fib_dyn(5))   # 5
    print(fib_dyn(6))   # 8