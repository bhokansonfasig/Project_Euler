from problem018 import load_triangle,find_best_path

if __name__ == '__main__':
    triangle = load_triangle('problem018_triangle.txt')
    triangle.reverse()
    for i in range(len(triangle)):
        for j in range(i):
            triangle[i].append('0')
        # print(len(triangle[i]))
    starts = triangle[0]
    # print(triangle[14][14])

    best_total = 0
    for i in range(len(starts)):
        for tot_factor in range(2):
            for max_factor in range(2):
                for next_factor in range(2):
                    total = find_best_path(triangle,tot_factor,max_factor,
                                            next_factor,3,(0,i))
                    if total>best_total:
                        print(tot_factor,max_factor,next_factor,"=>",total)
                        best_total = total
