def square_digits(n):
    total = 0
    while n != 0:
        total += (n % 10)**2
        n //= 10
    return total
