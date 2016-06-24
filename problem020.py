from problem016 import hand_multiply

if __name__ == '__main__':
    digits = ['1']
    for i in range(1,101):
        digits = hand_multiply(digits,i)
    number = ''
    total = 0
    for digit in reversed(digits):
        number += digit
        total += int(digit)
    print(number, "=>", total)
