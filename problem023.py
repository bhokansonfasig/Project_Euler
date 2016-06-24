from problem021 import get_divisors

def is_perfect(number):
    divisors = get_divisors(number)
    return sum(divisors[:-1])==number

def is_abundant(number):
    divisors = get_divisors(number)
    return sum(divisors[:-1])>number

def get_abundant_numbers(maximum):
    abundants = []
    for i in range(1,maximum):
        if is_abundant(i):
            abundants.append(i)
    return abundants

if __name__ == '__main__':
    abundants = get_abundant_numbers(30000)
    total = 0
    for i in range(1,28124):
        if i%1000==0:
            print(i)
        sum_of_abundants = False
        for abundant in abundants:
            candidate = i - abundant
            if candidate<12:
                break
            if candidate in abundants:
                sum_of_abundants = True
                break
        if not(sum_of_abundants):
            total += i
    print("Total:",total)
