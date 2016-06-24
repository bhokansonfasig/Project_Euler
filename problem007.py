def generate_n_primes(n):
    primes = [2]
    number = 2
    while len(primes)<n:
        number += 1
        add_to_primes = True
        for prime in primes:
            if number%prime==0:
                add_to_primes = False
                break
        if add_to_primes:
            primes.append(number)
    return primes

if __name__ == '__main__':
    primes = generate_n_primes(10001)
    print(primes[len(primes)-1])
