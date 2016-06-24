from problem003 import generate_primes

if __name__ == '__main__':
    primes = generate_primes(2000000)
    total = 0
    for prime in primes:
        total += prime
    print(total)
