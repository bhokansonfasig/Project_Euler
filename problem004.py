def is_palindrome(object):
    string = str(object)
    length = len(string)
    palindromic = True
    for i in range(length):
        if string[i]!=string[length-1-i]:
            palindromic = False
            break
    return palindromic

def n_digit_numbers(digits):
    return range(10**digits)

if __name__ == '__main__':
    digits = 3
    palindromes = []
    for i in n_digit_numbers(digits):
        for j in n_digit_numbers(digits):
            if is_palindrome(i*j):
                palindromes.append(i*j)
    print(max(palindromes))
