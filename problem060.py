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

if __name__ == '__main__':
    primes = read_primes('primes_table.txt')

    smallest_sum = 1000000

    found_sets = []
    for i in primes:
        if i==2:
            continue
        if i>10:
            break
        print("\n",i,":",sep="")
        for j in primes:
            if j<=i:
                continue
            if j>10:
                break
            print(j)
            for k in primes:
                if k<=j:
                    continue
                if k>100:
                    break
                print(k)
                for l in primes:
                    if l<=k:
                        continue
                    if l>300:
                        break
                    for m in primes:
                        if m<=l:
                            continue
                        if m>1000 or i+j+k+l+m>smallest_sum:
                            break
                        prime_set = [i,j,k,l,m]
                        if test_concatenated_prime(prime_set):
                            found_sets.append(prime_set)
                            smallest_sum = sum(prime_set)
                            print(prime_set,"=>",smallest_sum)

    print("Found",len(found_sets),"possibilities.")

    for prime_set in found_sets:
        print(prime_set,"=>",sum(prime_set))
