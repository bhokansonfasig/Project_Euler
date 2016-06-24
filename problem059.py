def get_cipher(filename):
    f = open(filename,"r")
    line = f.read()
    number_srings = line.split(",")
    numbers = []
    for number in number_srings:
        numbers.append(int(number))
    return numbers

def check_for_that(numbers):
    possible_thats = []
    for i in range(len(numbers)-3):
        if numbers[i]==numbers[i+3]:
            possible_thats.append([i,numbers[i:i+4]])
    return possible_thats

if __name__ == '__main__':
    numbers = get_cipher('problem059cipher.txt')
    possible_thats = check_for_that(numbers)
    print(len(possible_thats),"possible 'that's")
    # t = 116
    password_candidates = []
    for that in possible_thats:
        number = that[1][0]^116
        password_candidates.append(str(chr(number)))
    candidate_frequencies = {}
    for candidate in password_candidates:
        if candidate not in candidate_frequencies.keys():
            candidate_frequencies[candidate] = 1
        else:
            candidate_frequencies[candidate] += 1
    password_candidate_ints = []
    for candidate, frequency in candidate_frequencies.items():
        candidate_int = ord(candidate)
        if frequency>1 and candidate_int>=97 and candidate_int<123:
            password_candidate_ints.append(candidate_int)
            print(candidate,frequency)

    # for candidate_int_1 in password_candidate_ints:
    #     for candidate_int_2 in password_candidate_ints:
    #         for candidate_int_3 in password_candidate_ints:
    #             print(str(chr(candidate_int_1)),str(chr(candidate_int_2)),
    #                     str(chr(candidate_int_3)),":", sep="")
    #             for that in possible_thats:
    #                 if str(chr(candidate_int_1^that[1][0]))=="t":
    #                     print("candidate found -> ",end="")
    #                     if str(chr(candidate_int_2^that[1][1]))=="h":
    #                         print("good so far -> ",end="")
    #                         if str(chr(candidate_int_3^that[1][2]))=="a":
    #                             print("we did it!")
    #                         else:
    #                             print()
    #                     else:
    #                         print()

    password = ['g','o']
    for i in range(97,123):
        for that in possible_thats:
            if str(chr(ord(password[0])^that[1][0]))=="t" and \
                str(chr(ord(password[1])^that[1][1]))=="h" and \
                str(chr(i^that[1][2]))=="e":
                print(str(chr(i)),"-> e")
            else:
                print("no",end="")



    # for number in range(97,123):
    #     char = str(chr(number))
    #     print(ord(char),"=>",char)
