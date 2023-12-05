def generate_primes(limit):
    primes = []
    is_prime = [True] * (limit + 1)
    
    for num in range(2, int(limit**0.5) + 1):
        if is_prime[num]:
            primes.append(num)
            for multiple in range(num * num, limit + 1, num):
                is_prime[multiple] = False

    for num in range(int(limit**0.5) + 1, limit + 1):
        if is_prime[num]:
            primes.append(num)

    return primes

def find_nth_prime(n):
    limit = 110000  # A rough estimate to cover the 10001st prime
    primes = generate_primes(limit)

    while len(primes) < n:
        limit *= 2
        primes = generate_primes(limit)

    return primes[n - 1]

# Find the 10001st prime number
result = find_nth_prime(10001)
print(result)



# def is_prime(n)->bool:
#     if n == 0 or n == 1:
#         return False
#     for i in range(2,n):
#         if n % i == 0:
#             return False
#     return True

# def n_primes(n)->bool:
#     arr = []
#     i = 1
#     while n > 0:
#         if is_prime(i):
#            arr.append(i)
#            n-=1
#         i+=1
#     return arr


# arr = n_primes(10001)

# for i, j in enumerate(arr):
#     print(f"{i} : {j}")

