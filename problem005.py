if __name__ == '__main__':
    i = 20
    divisible_by_all = False
    while not(divisible_by_all):
        i += 1
        divisible_by_all = True
        for j in range(2,21):
            if i%j!=0:
                divisible_by_all = False
                break
        if i%10000000==0:
            print(i)

    print(i)
