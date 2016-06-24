def get_sorted_names(filename):
    f = open(filename,'r')
    quote_names = f.read().split(',')
    # names = []
    # for i in range(len(quote_names)):
    #     names.append([i,quote_names[i].replace('"','')])
    # names.sort(key=lambda x: x[1])
    # return names
    names = []
    for name in quote_names:
        names.append(name[1:-1])
    return sorted(names)


if __name__ == '__main__':
    names = get_sorted_names('problem022_names.txt')
    alphabet = ['','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O',
                'P','Q','R','S','T','U','V','W','X','Y','Z']
    total = 0
    for i in range(len(names)):
        score = 0
        for letter in names[i]:
            score += alphabet.index(letter)
        #     print(letter,alphabet.index(letter))
        # print(i+1,"*",score,"= ",end="")
        score *= i+1
        # print(score)
        total += score

    print(total)
