def get_cipher(filename):
    f = open(filename,"r")
    line = f.read()
    number_srings = line.split(",")
    numbers = []
    for number in number_srings:
        numbers.append(int(number))
    return numbers

def search_word(cipher_numbers, word):
    possible_keys = []
    for i in range(97,123):
        for j in range(97,123):
            for k in range(97,123):
                for l in range(len(cipher_numbers)-len(word)):
                    found_word = True
                    key = [i,j,k]
                    for m in range(len(word)):
                        if str(chr(key[m%3]^cipher_numbers[l+m]))!=word[m]:
                            found_word = False
                            break
                    if found_word:
                        possible_keys.append([str(chr(i)),str(chr(j)),
                                                str(chr(k))])
                        break
    return possible_keys

def decode_cipher(cipher_numbers,key):
    keylen = len(key)
    decoded_text = ""
    for i in range(len(cipher_numbers)):
        decoded_text += str(chr(ord(key[i%keylen])^cipher_numbers[i]))
    return decoded_text

if __name__ == '__main__':
    numbers = get_cipher('problem059cipher.txt')

    common_words = ['the','be','to','of','and','in','that','have','it','for']

    most_found = 0
    for i in range(97,123):
        for j in range(97,123):
            for k in range(97,123):
                key = [str(chr(i)),str(chr(j)),str(chr(k))]
                possible_text = decode_cipher(numbers,key)
                found_words = 0
                for word in common_words:
                    if possible_text.find(word)>-1:
                        found_words += 1
                if found_words>most_found:
                    most_found = found_words
                    best_key = key

    decoded_text = decode_cipher(numbers,best_key)
    print(best_key,"\n",decoded_text,"\n")

    total = 0
    for char in decoded_text:
        total += ord(char)

    print("Sum of ASCII:",total)
