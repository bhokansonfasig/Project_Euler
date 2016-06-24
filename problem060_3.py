from math import sqrt

def read_primes(filename='primes_table.txt'):
    primes = []
    f = open(filename,'r')
    for line in f:
        stripped = line.rstrip()
        primes.append(int(stripped))
    return primes

def test_concatenated_prime_set(prime_set):
    for a in prime_set:
        for b in prime_set:
            if a!=b:
                test = int(str(a)+str(b))
                if not(is_prime(test)):
                    return False
    return True

def get_concatenating_primes(number,primes):
    concatenating_primes = []
    for i in primes:
        candidate_1 = int(str(i)+str(number))
        candidate_2 = int(str(number)+str(i))
        if is_prime(candidate_1) and is_prime(candidate_2):
            concatenating_primes.append(i)
    return concatenating_primes

def is_concatenating_prime(prime1,prime2):
    return is_prime(int(str(prime1)+str(prime2))) and \
            is_prime(int(str(prime2)+str(prime1)))

def is_prime(number):
    for i in range(2,int(sqrt(number)+2)):
        if number%i==0:
            return False
    return True


if __name__ == '__main__':
    primes = read_primes('primes_table.txt')
    print(len(primes),"total primes.")

    max_prime_scale = 2

    max_i = max_prime_scale*100
    max_j = max_prime_scale*500
    max_k = max_prime_scale*2000
    max_l = max_prime_scale*2000
    max_m = max_prime_scale*10000
    smallest_sum = 34427
    print("Checking primes up to",primes[max_i],primes[max_j],primes[max_k],
                                    primes[max_l],primes[max_m])

    found_sets = []

    progress_index = 5

    for i in range(max_i):
        # print("\n",primes[i],":",sep="")
        if i*100/max_i>progress_index:
            print(progress_index,"% done",sep="")
            progress_index += 5

        # related_primes = get_concatenating_primes(i,primes[:max_index])
        # print(related_primes)

        for j in range(i,max_j):
            if not(is_concatenating_prime(primes[i],primes[j])):
                continue
            # print(j)

            # related_primes_2 = get_concatenating_primes(j,primes[:max_index])
            # print(related_primes_2)

            for k in range(j,max_k):
                if primes[i]+primes[j]+primes[k] \
                        > smallest_sum:
                    break
                if not(is_concatenating_prime(primes[i],primes[k]) and \
                        is_concatenating_prime(primes[j],primes[k])):
                    continue

                # related_primes_3 = get_concatenating_primes(k,
                #                                         primes[:max_index])
                # print(related_primes_3)

                for l in range(k,max_l):
                    if primes[i]+primes[j]+primes[k]+primes[l] \
                            > smallest_sum:
                        break
                    if not(is_concatenating_prime(primes[i],primes[l]) and \
                            is_concatenating_prime(primes[j],primes[l]) and \
                            is_concatenating_prime(primes[k],primes[l])):
                        continue

                    # related_primes_4 = get_concatenating_primes(l,
                    #                                     primes[:max_index])
                    # print(related_primes_4)

                    for m in range(l,max_m):
                        if primes[i]+primes[j]+primes[k]+primes[l]+primes[m] \
                                > smallest_sum:
                            break
                        if not(is_concatenating_prime(primes[i],primes[m]) and \
                                is_concatenating_prime(primes[j],primes[m]) and \
                                is_concatenating_prime(primes[k],primes[m]) and \
                                is_concatenating_prime(primes[l],primes[m])):
                            continue
                        prime_set = [primes[i],primes[j],primes[k],primes[l],
                                        primes[m]]
                        if test_concatenated_prime_set(prime_set):
                            found_sets.append(prime_set)
                            smallest_sum = sum(prime_set)
                            print(prime_set,"=>",smallest_sum)

    print("Found",len(found_sets),"possibilities.")

    for prime_set in found_sets:
        print(prime_set,"=>",sum(prime_set))
