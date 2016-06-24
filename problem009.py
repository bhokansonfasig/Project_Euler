if __name__ == '__main__':
    found_triplet = False
    for i in range(1,1000):
        for j in range(1,1000):
            k = 1000 - i - j
            if k<1:
                break
            if i**2+j**2==k**2:
                found_triplet = True
                break
        if found_triplet:
            break
    if found_triplet:
        print(i,j,k,"=>",i*j*k)
