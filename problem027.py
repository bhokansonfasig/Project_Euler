from problem060_3 import read_primes, is_prime

def largest_n(a,b):
    n = 0
    while n<100000:
        value = n**2 + a*n + b
        if value<2:
            break
        if not(is_prime(value)):
            break
        n += 1
    return n-1


if __name__ == '__main__':
    primes = read_primes()
    b_values = [x for x in primes if x<1000]
    a_values = [0]
    for i in range(1,1000):
        a_values.append(i)
        a_values.append(-i)

    best_coefficients = [0,0,0]
    for a in a_values:
        for b in b_values:
            # if a%10==0:
            #     print(a,b)
            n = largest_n(a,b)
            if n>best_coefficients[2]:
                best_coefficients = [a,b,n]
                print(best_coefficients)
