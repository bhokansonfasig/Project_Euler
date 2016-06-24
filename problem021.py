from math import sqrt

def get_divisors(number):
    divisors = []
    for i in range(1,int(sqrt(number)+2)):
        if number%i==0:
            if not(i in divisors):
                divisors.append(i)
            if not(int(number/i) in divisors):
                divisors.append(int(number/i))
    return sorted(divisors)

if __name__ == '__main__':
    amicable_numbers = []
    for i in range(1,10000):
        sum_1 = sum(get_divisors(i))-i
        sum_2 = sum(get_divisors(sum_1))-sum_1
        if sum_2==i and sum_1!=i:
            if not(i in amicable_numbers):
                amicable_numbers.append(i)
                amicable_numbers.append(sum_1)

    print(amicable_numbers)
    print(sum(amicable_numbers))
