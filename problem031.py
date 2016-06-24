def rec_gather_coins(current_set):
    available_coins = [1,2,5,10,20,50,100,200]
    available_coins.reverse()
    goal = 200
    tracker[0] += 1
    if tracker[0]%10000==0:
        print(len(all_starts),"starts  ",len(all_2e_sets),"sets found")
    if not(current_set in all_starts):
        all_starts.append(current_set)
        for coin in available_coins:
            value = sum(current_set)
            new_set = current_set+[coin]
            new_set.sort()
            if value+coin==goal and not(new_set in all_2e_sets):
                all_2e_sets.append(new_set)
            elif value+coin<goal:
                rec_gather_coins(new_set)


if __name__ == '__main__':
    all_2e_sets = []
    all_starts = []
    tracker = [0]
    rec_gather_coins([])
    # print(all_2e_sets)
    print(len(all_2e_sets))
