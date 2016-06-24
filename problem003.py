from math import sqrt

def generate_primes(maximum):
    primes = [2]
    for number in range(3,maximum+1):
        add_to_primes = True
        for prime in primes:
            if number%prime==0:
                add_to_primes = False
                break
        if add_to_primes:
            primes.append(number)
    return primes

def partial_factorize(number):
    factors = []
    maximum = int(sqrt(number)+1)
    primes = generate_primes(maximum)
    while not(number in primes):
        got_all_primes = True
        for prime in primes:
            if number%prime==0:
                factors.append(prime)
                number = number / prime
                got_all_primes = False
                break
            if prime>number:
                break
        if got_all_primes:
            break
    factors.append(int(number))
    return factors

def full_factorize(number):
    factors = []
    initial_factors = partial_factorize(number)
    for factor in initial_factors:
        secondary_factors = partial_factorize(factor)
        for other_factor in secondary_factors:
            factors.append(other_factor)
    return factors

if __name__ == '__main__':
    number = 600851475143
    print("The factors of",number,"are",full_factorize(number))
