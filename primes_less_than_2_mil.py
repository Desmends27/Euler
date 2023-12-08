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


vals = generate_primes(2_000_000)
_sum= 0
for i in vals:
  _sum += i

print(_sum)
