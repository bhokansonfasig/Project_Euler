# from problem060_3 import read_primes

def hand_divide(numerator,denominator):
    # num_dig = list(str(numerator))
    d = denominator
    # den_dig = list(str(denominator))
    res = int(numerator/denominator)
    res_dig = list(str(res))
    res_dig.append('.')
    decimal_pos = len(res_dig)
    num_dig = list(str(numerator-res*denominator))
    dig_index = 0
    while num_dig!=['0']:
        dig_index += 1
        # print(res_dig)
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
    return eval(number)

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


if __name__ == '__main__':
    # primes = read_primes()
    longest_period = [0,0]
    # for i in reversed(primes):
    for i in range(1000,1,-1):
        if i>1000:
            continue
        print(i)
        digits = hand_divide(1,i)
        decimal_start = digits.index('.')
        backwards_digits = digits[decimal_start:]
        backwards_digits.reverse()
        for j in range(len(backwards_digits)):
            period = check_period(backwards_digits[:j])
            if period>0:
                break
        if period>longest_period[1]:
            longest_period = ['1/'+str(i),period]
        if period>longest_period[1]*.75:
            print('1/'+str(i), '-', period, '('+str(len(digits))+')')
