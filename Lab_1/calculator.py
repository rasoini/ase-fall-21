#calculator.py

def sum(m, n):
    if n < 0:
        for i in range(-n):
            m -= 1
    else:
        for i in range(n):
            m += 1
    return m

def divide(m, n):
    if (n == 0):
        raise ZeroDivisionError

    k = 0
    isNeg = (m > 0 and n < 0) or (m < 0 and n > 0)
    n = abs(n)
    m = abs(m)

    while m >= n:
        m -= n
        k += 1

    if isNeg:
        return -k
    return k

if __name__ == "__main__":
    print(divide(28, -7))
