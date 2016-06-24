from math import sqrt

def generate_fibonacci(maximum):
    sequence = [0]
    new_num = 1
    while new_num<=maximum:
        sequence.append(new_num)
        index = len(sequence)
        new_num = sequence[index-1]+sequence[index-2]
    return sequence


def generate_primes(maximum=100000):
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


def generate_n_primes(n=10000):
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


def read_primes(filename='primes_table.txt'):
    primes = []
    f = open(filename,'r')
    for line in f:
        stripped = line.rstrip()
        primes.append(int(stripped))
    return primes


def is_prime(number):
    if number<2:
        return False
    if number==2:
        return True
    for i in range(2,int(sqrt(number)+2)):
        if number%i==0:
            return False
    return True


def is_palindrome(thing):
    string = str(thing)
    length = len(string)
    palindromic = True
    for i in range(length):
        if string[i]!=string[length-1-i]:
            palindromic = False
            break
    return palindromic


def is_perfect(number):
    divisors = get_divisors(number)
    return sum(divisors[:-1])==number


def is_abundant(number):
    divisors = get_divisors(number)
    return sum(divisors[:-1])>number


def get_divisors(number):
    divisors = []
    for i in range(1,int(sqrt(number)+2)):
        if number%i==0:
            if not(i in divisors):
                divisors.append(i)
            if not(int(number/i) in divisors):
                divisors.append(int(number/i))
    return sorted(divisors)


def get_factors(number):
    divisors = get_divisors(number)
    return [x for x in divisors if is_prime(x)]


def get_all_factors(number):
    unique_factors = get_factors(number)
    factors = []
    while number>=1:
        found_additional = False
        for factor in unique_factors:
            if number%factor==0:
                number = number/factor
                factors.append(factor)
                found_additional = True
                break
        if not(found_additional):
            break
    factors.sort()
    return factors


def hand_add(digits1,digits2):
    digits_1 = digits1[:]
    digits_2 = digits2[:]
    digits_1.reverse()
    digits_2.reverse()
    length_1 = len(digits_1)
    length_2 = len(digits_2)
    if length_1<length_2:
        shorter = digits_1
        longer = digits_2
    else:
        shorter = digits_2
        longer = digits_1
    new_digits = []
    for i in range(len(longer)):
        if i<len(shorter):
            new_digits.append(str(int(digits_1[i])+int(digits_2[i])))
        else:
            new_digits.append(str(longer[i]))
    i = 0
    while i < len(new_digits):
        dig_len = len(new_digits[i])
        if dig_len>1:
            for j in range(dig_len-1):
                while i+dig_len-j>len(new_digits):
                    new_digits.append('0')
                new_digits[i+dig_len-1-j] = str(int(new_digits[i+dig_len-1-j])+int(new_digits[i][j]))
            new_digits[i] = new_digits[i][dig_len-1]
        i += 1
    new_digits.reverse()
    return new_digits


def hand_multiply(digits,number):
    digits_rev = digits[:]
    digits_rev.reverse()
    new_digits = []
    for digit in digits_rev:
        new_digits.append(str(number*int(digit)))
    i = 0
    while i < len(new_digits):
        dig_len = len(new_digits[i])
        if dig_len>1:
            for j in range(dig_len-1):
                while i+dig_len-j>len(new_digits):
                    new_digits.append('0')
                new_digits[i+dig_len-1-j] = str(int(new_digits[i+dig_len-1-j])+int(new_digits[i][j]))
            new_digits[i] = new_digits[i][dig_len-1]
        i += 1
    new_digits.reverse()
    return new_digits


def hand_divide(numerator,denominator):
    d = denominator
    res = int(numerator/denominator)
    res_dig = list(str(res))
    res_dig.append('.')
    decimal_pos = len(res_dig)
    num_dig = list(str(numerator-res*denominator))
    dig_index = 0
    while num_dig!=['0']:
        dig_index += 1
        num_dig.append('0')
        n = undigit(num_dig)
        res = int(n/d)
        res_dig.extend(list(str(res)))
        num_dig = list(str(n-res*d))
        backwards_res = res_dig[decimal_pos:]
        backwards_res.reverse()
        period = -1
        if dig_index%100==0:
            for i in range(len(backwards_res)):
                period = check_period(backwards_res[:i])
                if period>0:
                    break
        if period>0:
            if check_threepeating(res_dig[-3*period:],period):
                break
    return res_dig


def undigit(digits):
    number = ''
    for digit in digits:
        number += digit
    return float(number)


def check_period(repeating_list):
    length = len(repeating_list)
    shortest_period = length
    for period in range(1,int(length/2)+1):
        repeating = True
        for j in range(length-period):
            if repeating_list[j]!=repeating_list[j+period]:
                repeating = False
                break
        if repeating:
            shortest_period = period
            break
    if shortest_period==length:
        shortest_period = -1
    return shortest_period


def check_threepeating(candidate,period):
    if period<1:
        return False
    repeating = True
    for i in range(len(candidate)-2*period):
        if candidate[i]!=candidate[i+period] or \
        candidate[i]!=candidate[i+2*period]:
            repeating = False
            break
    return repeating


def spell_small_number(number,use_and=True):
    if number>=1000 or number<0:
        print(number,"out of supported range.")
        return ''
    else:
        ones = ['zero','one','two','three','four','five','six','seven',
                    'eight','nine']
        teens = ['ten','eleven','twelve','thirteen','fourteen','fifteen',
                    'sixteen','seventeen','eighteen','nineteen']
        tens = ['zero','ten','twenty','thirty','forty','fifty','sixty',
                    'seventy','eighty','ninety']
        spelled = ''
        num_str = str(number)
        length = len(num_str)
        if length==3:
            if num_str[-2:]=='00':
                spelled += ones[int(num_str[-3])] + ' hundred'
                length = 0
            else:
                spelled += ones[int(num_str[-3])] + ' hundred '
                if use_and:
                    spelled += 'and '
                length = 2
        if length==2:
            if num_str[-2]=='1':
                spelled += teens[int(num_str[-1])]
                length = 0
            elif num_str[-1]=='0':
                spelled += tens[int(num_str[-2])]
                length = 0
            elif num_str[-2]=='0':
                length = 1
            else:
                spelled += tens[int(num_str[-2])] + '-'
                length = 1
        if length==1:
            spelled += ones[int(num_str[-1])]
    return spelled


def spell_number(number):
    if number>=1000000000000000000000000000000 or number<0:
        print(number,"out of supported range.")
        return ''
    else:
        illions = ['thousand','million','billion','trillion','quadrillion',
                    'quintillion','sextillion','septillion','octillion',
                    'nonillion']
        spelled = ''
        num_str = str(number)
        length = len(num_str)
        location = length%3
        if location>0 and length>3:
            prefix = num_str[:length%3]
            spelled += spell_small_number(int(prefix),use_and=False) + ' ' + \
                        illions[int((length-location)/3)-1] + ' '
        while location+3<length:
            portion = num_str[location:location+3]
            if portion!='000':
                spelled +=  spell_small_number(int(portion),use_and=False) + \
                                ' ' + illions[int((length-location)/3)-2] + ' '
            location += 3
        if num_str[-3:]!='000':
            if length>3:
                if num_str[-3]=='0':
                    spelled += 'and '
            spelled += spell_small_number(int(num_str[-3:]))
    return spelled
