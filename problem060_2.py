def read_primes(filename='primes_table.txt'):
    primes = []
    f = open(filename,'r')
    for line in f:
        stripped = line.rstrip()
        primes.append(int(stripped))
    return primes

def test_concatenated_prime(prime_set):
    for a in prime_set:
        for b in prime_set:
            if a!=b:
                test = int(str(a)+str(b))
                if not(test in primes):
                    # print(test,"is not prime")
                    return False
    return True

def get_related_primes(num,primes,prev_full_related_primes):
    related_primes = []
    full_related_primes = []
    num_str = str(num)
    for i in primes:
        if i<=num:
            continue
        i_str = str(i)
        loc = i_str.find(num_str)
        if loc==0:
            new_num = int(i_str[len(num_str):])
            if not(new_num in related_primes) and (new_num in primes) and \
            (i in prev_full_related_primes):
                related_primes.append(new_num)
                full_related_primes.append(i)
        elif loc+len(num_str)==len(i_str):
            new_num = int(i_str[:loc])
            if not(new_num in related_primes) and (new_num in primes) and \
            (i in prev_full_related_primes):
                related_primes.append(new_num)
                full_related_primes.append(i)
    return related_primes, full_related_primes

if __name__ == '__main__':
    primes = read_primes('primes_table.txt')
    print(len(primes),"total primes")

    smallest_sum = 1000000

    found_sets = []

    for i in primes:
        if i==2:
            continue
        if i>10:
            break
        print("\n",i,":",sep="")
        related_primes, full_related_primes =\
            get_related_primes(i,primes,primes)
        print(len(related_primes),"related primes")
        for j in related_primes:
            if j<=i:
                continue
            if j>30:
                break
            print(j)
            second_related_primes, second_full_related_primes =\
                get_related_primes(j,primes,full_related_primes)
            # for prime in new_primes:
            #     if prime in related_primes:
            #         second_related_primes.append(prime)
            print(len(second_related_primes),"second related primes")
            for k in second_related_primes:
                if k<=j:
                    continue
                if k>1000:
                    break
                third_related_primes, third_full_related_primes =\
                    get_related_primes(k,primes,second_full_related_primes)
                # for prime in new_primes:
                #     if prime in second_related_primes:
                #         third_related_primes.append(prime)
                print(len(third_related_primes),"third related primes")
                for l in third_related_primes:
                    if l<=k:
                        continue
                    if l>1000:
                        break
                    fourth_related_primes, fourth_full_related_primes =\
                        get_related_primes(l,primes,third_full_related_primes)
                    # for prime in new_primes:
                    #     if prime in third_related_primes:
                    #         fourth_related_primes.append(prime)
                    # print(len(fourth_related_primes),"fourth related primes")
                    for m in fourth_related_primes:
                        if m<=l:
                            continue
                        if i+j+k+l+m>smallest_sum:
                            break
                        prime_set = [i,j,k,l,m]
                        if test_concatenated_prime(prime_set):
                            found_sets.append(prime_set)
                            smallest_sum = sum(prime_set)
                            print(prime_set,"=>",smallest_sum)

    print("Found",len(found_sets),"possibilities.")

    for prime_set in found_sets:
        print(prime_set,"=>",sum(prime_set))
