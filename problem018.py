def load_triangle(filename):
    triangle = []
    f = open(filename,'r')
    for line in f:
        triangle.append(line.split())
    return triangle

def traverse_left(coord):
    return (coord[0]+1,coord[1])

def traverse_right(coord):
    return (coord[0]+1,coord[1]+1)

def look_left(coord,triangle,depth):
    total = 0
    maximum = 0
    if coord[0]+depth>=len(triangle):
        max_row = len(triangle) - coord[0]
    else:
        max_row = depth + 1
    for row in range(1,max_row):
        for col in range(row):
            number = int(triangle[coord[0]+row][coord[1]+col])
            total += number
            if number>maximum:
                maximum = number
    return total, maximum

def look_right(coord,triangle,depth):
    total = 0
    maximum = 0
    if coord[0]+depth>=len(triangle):
        max_row = len(triangle) - coord[0]
    else:
        max_row = depth + 1
    for row in range(1,max_row):
        for col in range(row):
            try:
                number = int(triangle[coord[0]+row][coord[1]+col+1])
            except:
                print(coord[0],row,coord[1],col)
            total += number
            if number>maximum:
                maximum = number
    return total, maximum

def find_best_path(triangle,tot_factor,max_factor,next_factor,max_depth,start):
    biggest_total = 0
    for explore_depth in range(2,max_depth):
        total = find_path(triangle,tot_factor,max_factor,next_factor,
                            explore_depth,start)
        # print("Total:",total)
        if total>biggest_total:
            biggest_total = total
    return biggest_total

def find_path(triangle,tot_factor,max_factor,next_factor,explore_depth,start):
    rows = len(triangle)
    coordinate = start
    total = 0
    while coordinate[0]<rows:
        # print(triangle[coordinate[0]][coordinate[1]],end=" ")
        total += int(triangle[coordinate[0]][coordinate[1]])
        l_next, tmp = look_left(coordinate,triangle,1)
        r_next, tmp = look_right(coordinate,triangle,1)
        l_tot, l_max = look_left(coordinate,triangle,explore_depth)
        r_tot, r_max = look_right(coordinate,triangle,explore_depth)
        l_calc = tot_factor*l_tot/(explore_depth**2-explore_depth) + \
                    max_factor*l_max + next_factor*l_next
        r_calc = tot_factor*r_tot/(explore_depth**2-explore_depth) + \
                    max_factor*r_max + next_factor*r_next
        if l_calc>r_calc:
            coordinate = traverse_left(coordinate)
        else:
            coordinate = traverse_right(coordinate)
    return total


if __name__ == '__main__':
    triangle = load_triangle('problem018_triangle.txt')

    best_total = 0
    for tot_factor in range(5):
        for max_factor in range(5):
            for next_factor in range(5):
                total = find_best_path(triangle,tot_factor,max_factor,
                                        next_factor,len(triangle),(0,0))
                if total>best_total:
                    print(tot_factor,max_factor,next_factor,"=>",total)
                    best_total = total
