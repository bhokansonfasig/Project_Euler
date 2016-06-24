def get_lex_permutation(index):
    count = 0
    for i_0 in range(10):
        for i_1 in range(10):
            if i_1==i_0:
                continue
            for i_2 in range(10):
                if i_2==i_1 or i_2==i_0:
                    continue
                for i_3 in range(10):
                    if i_3==i_2 or i_3==i_1 or i_3==i_0:
                        continue
                    for i_4 in range(10):
                        if i_4==i_3 or i_4==i_2 or i_4==i_1 or i_4==i_0:
                            continue
                        for i_5 in range(10):
                            if i_5==i_4 or i_5==i_3 or i_5==i_2 or i_5==i_1 or \
                            i_5==i_0:
                                continue
                            for i_6 in range(10):
                                if i_6==i_5 or i_6==i_4 or i_6==i_3 or \
                                i_6==i_2 or i_6==i_1 or i_6==i_0:
                                    continue
                                for i_7 in range(10):
                                    if i_7==i_6 or i_7==i_5 or i_7==i_4 or \
                                    i_7==i_3 or i_7==i_2 or i_7==i_1 or \
                                    i_7==i_0:
                                        continue
                                    for i_8 in range(10):
                                        if i_8==i_7 or i_8==i_6 or i_8==i_5 or \
                                        i_8==i_4 or i_8==i_3 or i_8==i_2 or \
                                        i_8==i_1 or i_8==i_0:
                                            continue
                                        for i_9 in range(10):
                                            if i_9==i_8 or i_9==i_7 or \
                                            i_9==i_6 or i_9==i_5 or \
                                            i_9==i_4 or i_9==i_3 or \
                                            i_9==i_2 or i_9==i_1 or i_9==i_0:
                                                continue
                                            count += 1
                                            if count==index:
                                                return [i_0,i_1,i_2,i_3,i_4,
                                                        i_5,i_6,i_7,i_8,i_9]


if __name__ == '__main__':
    perm = get_lex_permutation(1000000)
    for i in perm:
        print(i,end="")
    print()
