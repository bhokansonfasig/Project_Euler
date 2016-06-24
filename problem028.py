if __name__ == '__main__':
    total = 1
    i = 1
    dimension = 1001
    for half_side_len in range(int(dimension/2)):
        for j in range(4):
            i += half_side_len*2 + 2
            total += i

    print(total)
