import math

primes = [2, 3]

def find_primes(n):
    for i in range(primes[-1] + 2, n, 2):
        prime = True
        for p in primes:
            if i % p == 0:
                prime = False
                break
        if prime:
            primes.append(i)

def divisors(n):
    if n == 1 or n == 0:
        return []
    lim = math.ceil(math.sqrt(n))
    divs = []
    for i in range(2, lim):
        if n % i == 0:
            divs.append(i)
            divs.append(math.floor(n / i))
    if lim * lim == n:
        divs.append(lim)
    divs.sort()
    return divs
