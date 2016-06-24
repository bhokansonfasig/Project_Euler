def follow_collatz(number, count):
    count += 1
    if number<=1:
        return count
    elif number%2:
        return follow_collatz(3*number+1,count)
    else:
        return follow_collatz(int(number/2),count)

if __name__ == '__main__':
    max_length = 0
    for i in range(1,1000000):
        length = follow_collatz(i,0)
        if length>max_length:
            print(i,"=>",length)
            max_length = length
