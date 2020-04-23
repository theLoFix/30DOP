# Write a generator that generates prime numbers in a specified range.

def gen_primes(limit):
    for dividend in range(2, limit + 1):
        for divisor in range(2, dividend):
            if dividend % divisor == 0:
                break
        else:
            yield dividend

primes = gen_primes(101)

print(next(primes))
print(next(primes))
print(next(primes))


