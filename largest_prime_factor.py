def largest_factor(n) -> int:
    i = 2
    while i * i < n:
        while n % i == 0:
            n = n / i
        i = i + 1
    return n

print(largest_factor(600851475143))