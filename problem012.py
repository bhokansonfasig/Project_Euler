from problem003 import partial_factorize
from math import factorial
import sys

def all_divisors(number):
    divisors = [1]
    for i in range(2,number+1):
        if number%i==0:
            divisors.append(i)
    return divisors

def num_divisors(number):
    if number==1:
        return 1
    factors = partial_factorize(number)
    unique_factors = []
    num_factors = len(factors)
    divisor_count = 2**num_factors
    for factor in factors:
        if not(factor in unique_factors):
            unique_factors.append(factor)
    num_unique_factors = len(unique_factors)
    num_non_unique = num_factors - num_unique_factors
    for factor in unique_factors:
        duplicate_count = factors.count(factor)
        for i in range(1,duplicate_count):
            divisor_count -= factorial(a)/\
                                (factorial(b)*factorial(a-b)) #(aCb)
    print(factors)
    return int(divisor_count+1)


if __name__ == '__main__':
    # print(num_divisors(eval(sys.argv[1])))
    print(all_combinations([1,2,3]))

    # max_divisors = 0
    # triangle_number = 0
    # i = 1
    # while max_divisors<5:
    #     i += 1
    #     triangle_number += i
    #     divisors = len(all_divisors(triangle_number))
    #     if divisors>max_divisors:
    #         print(triangle_number,"is the first triangle number with",
    #                 divisors,"divisors")
    #         max_divisors = divisors
