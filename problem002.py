def generate_fibonacci(maximum):
    sequence = [1]
    new_num = 2
    while new_num<=maximum:
        sequence.append(new_num)
        index = len(sequence)
        new_num = sequence[index-1]+sequence[index-2]
    return sequence


if __name__ == '__main__':
    sequence = generate_fibonacci(4000000)
    total = 0
    for number in sequence:
        if number%2==0:
            total += number
    print(total)
