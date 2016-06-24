if __name__ == '__main__':
    number_file = open("problem013_numbers.txt",'r')
    numbers = []
    for line in number_file:
        numbers.append(int(line[:15]))

    total = sum(numbers)
    total_string = str(total)+"0"*35

    print(total_string)
