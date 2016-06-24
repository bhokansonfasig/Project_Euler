def spell_small_number(number,use_and=True):
    if number>=1000 or number<0:
        print(number,"out of supported range.")
        return ''
    else:
        ones = ['zero','one','two','three','four','five','six','seven',
                    'eight','nine']
        teens = ['ten','eleven','twelve','thirteen','fourteen','fifteen',
                    'sixteen','seventeen','eighteen','nineteen']
        tens = ['zero','ten','twenty','thirty','forty','fifty','sixty',
                    'seventy','eighty','ninety']
        spelled = ''
        num_str = str(number)
        length = len(num_str)
        if length==3:
            if num_str[-2:]=='00':
                spelled += ones[int(num_str[-3])] + ' hundred'
                length = 0
            else:
                spelled += ones[int(num_str[-3])] + ' hundred '
                if use_and:
                    spelled += 'and '
                length = 2
        if length==2:
            if num_str[-2]=='1':
                spelled += teens[int(num_str[-1])]
                length = 0
            # else:
            #     spelled += tens[int(num_str[-2])]
            #     length = int(num_str[-1]!='0')
            elif num_str[-1]=='0':
                spelled += tens[int(num_str[-2])]
                length = 0
            elif num_str[-2]=='0':
                length = 1
            else:
                spelled += tens[int(num_str[-2])] + '-'
                length = 1
        if length==1:
            spelled += ones[int(num_str[-1])]
    return spelled

def spell_number(number):
    if number>=1000000000000000000000000000000 or number<0:
        print(number,"out of supported range.")
        return ''
    else:
        illions = ['thousand','million','billion','trillion','quadrillion',
                    'quintillion','sextillion','septillion','octillion',
                    'nonillion']
        spelled = ''
        num_str = str(number)
        length = len(num_str)
        location = length%3
        if location>0 and length>3:
            prefix = num_str[:length%3]
            spelled += spell_small_number(int(prefix),use_and=False) + ' ' + \
                        illions[int((length-location)/3)-1] + ' '
        while location+3<length:
            portion = num_str[location:location+3]
            if portion!='000':
                spelled +=  spell_small_number(int(portion),use_and=False) + \
                                ' ' + illions[int((length-location)/3)-2] + ' '
            location += 3
        if num_str[-3:]!='000':
            if length>3:
                if num_str[-3]=='0':
                    spelled += 'and '
            spelled += spell_small_number(int(num_str[-3:]))
    return spelled


if __name__ == '__main__':
    total_chars = 0
    for i in range(1,1001):
        string = spell_number(i)
        string = string.replace(" ","")
        string = string.replace("-","")
        # print(string)
        total_chars += len(string)

    print(total_chars)
