def hand_add(digits1,digits2):
    digits_1 = digits1[:]
    digits_2 = digits2[:]
    digits_1.reverse()
    digits_2.reverse()
    length_1 = len(digits_1)
    length_2 = len(digits_2)
    if length_1<length_2:
        shorter = digits_1
        longer = digits_2
    else:
        shorter = digits_2
        longer = digits_1
    new_digits = []
    for i in range(len(longer)):
        if i<len(shorter):
            new_digits.append(str(int(digits_1[i])+int(digits_2[i])))
        else:
            new_digits.append(str(longer[i]))
    i = 0
    while i < len(new_digits):
        dig_len = len(new_digits[i])
        if dig_len>1:
            for j in range(dig_len-1):
                while i+dig_len-j>len(new_digits):
                    new_digits.append('0')
                new_digits[i+dig_len-1-j] = str(int(new_digits[i+dig_len-1-j])+int(new_digits[i][j]))
            new_digits[i] = new_digits[i][dig_len-1]
        # if dig_len==2:
        #     if i+1==len(new_digits):
        #         new_digits.append('0')
        #     new_digits[i+1] = str(int(new_digits[i+1])+1)
        #     new_digits[i] = new_digits[i][1]
        i += 1
    new_digits.reverse()
    return new_digits

if __name__ == '__main__':
    # print(hand_add(['2','1'],['1','3']))
    num_1 = [0]
    num_2 = [1]
    i = 1
    print("F1 =",1)
    while True:
        i += 1
        buf = num_2
        num_2 = hand_add(num_1,num_2)
        num_1 = buf
        if i%100==0:
            num_str = ""
            for digit in num_2:
                num_str += digit
            print("F",i," = ",num_str,sep="")
        if len(num_2)>=1000:
            print("Term",i,"has",len(num_2),"digits")
            break
