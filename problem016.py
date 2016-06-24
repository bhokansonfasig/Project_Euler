def multiply_by_2(digits):
    ones_digit = str(2*int(digits[0]))
    if len(ones_digit)==1:
        digits[0] = ones_digit
    else:
        digits[0] = ones_digit[1]
        add_new_digit = True
        for i in range(1,len(digits)):
            if digits[i]=='9':
                digits[i] = '0'
            else:
                digits[i] = str(int(digits[i])+1)
                add_new_digit = False
                break
        if add_new_digit:
            digits.append('1')

    return digits

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



if __name__ == '__main__':
    digits = ['1']
    for i in range(1000):
        digits = hand_multiply(digits,2)
    number = ''
    total = 0
    for digit in reversed(digits):
        number += digit
        total += int(digit)
    print(number, "=>", total)
