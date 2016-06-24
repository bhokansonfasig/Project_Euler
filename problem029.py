if __name__ == '__main__':
    power_list = []
    for a in range(2,101):
        for b in range(2,101):
            num = a**b
            if not(num in power_list):
                power_list.append(num)
    print(len(power_list))
