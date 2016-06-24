from problem021 import get_divisors
# import sys

if __name__ == '__main__':
    # print(get_divisors(eval(sys.argv[1])))
    # print(len(get_divisors(eval(sys.argv[1]))))

    max_divisors = 0
    triangle_number = 1
    i = 1
    while max_divisors<500:
        i += 1
        triangle_number += i
        divisors = len(get_divisors(triangle_number))
        if divisors>max_divisors:
            print(triangle_number,"is the first triangle number with",
                    divisors,"divisors")
            max_divisors = divisors
