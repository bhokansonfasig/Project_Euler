import sys
maximum = int(sys.argv[1])

primes = [2]
for number in range(3,maximum+1):
    add_to_primes = True
    for prime in primes:
        if number%prime==0:
            add_to_primes = False
            break
    if add_to_primes:
        primes.append(number)

print("Done generating table, now writing...")

table = open('primes_table_long.txt','w')

for prime in primes:
    table.write(str(prime)+"\n")

print("Finished")
