if __name__ == '__main__':
    power = 5
    digit_sums = []
    for digit1 in range(10):
        for digit2 in range(10):
            for digit3 in range(10):
                for digit4 in range(10):
                    for digit5 in range(10):
                        for digit6 in range(10):
                            number = int(str(digit1)+str(digit2)+str(digit3)+
                                         str(digit4)+str(digit5)+str(digit6))
                            if number>1 and number==digit1**power+\
                                    digit2**power+digit3**power+digit4**power+\
                                    digit5**power+digit6**power:
                                digit_sums.append(number)

    print(digit_sums)
    print(sum(digit_sums))
