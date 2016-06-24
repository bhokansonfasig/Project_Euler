from problem003 import full_factorize

if __name__ == '__main__':
    number = 1
    for i in range(2,21):
        if number%i!=0:
            number = number*i
    print(number)
    for i in range(2,21):
        print(number,"divisible by",i,number%i==0)
    factors = full_factorize(number)
    print(factors)
    for i in range(2,21):
        new_factors = full_factorize(i)
        for factor in new_factors:
            factors.remove(factor)
        print(factors)

# Doesn't work...
