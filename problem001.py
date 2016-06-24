def is_multiple(number,multiple):
    return number%multiple==0

if __name__ == '__main__':
    total = 0
    for i in range(1,1000):
        if is_multiple(i,3) or is_multiple(i,5):
            total += i
    print(total)
