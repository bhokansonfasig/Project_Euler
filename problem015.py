from random import random

# 2, 6, 20, 70, 252, 924, 3432, 12870
# >= 2^grid_size
# <= (grid_size+1)!

# http://math.stackexchange.com/questions/279993/probability-and-identical-balls-problem

if __name__ == '__main__':
    grid_size = 8
    i = 0
    possible_paths = []
    while True:
        i += 1
        x = 0
        y = 0
        if i%10000==0:
            print(len(possible_paths),"paths found.")
        path = []
        while x<grid_size and y<grid_size:
            if x==grid_size:
                y += 1
                path.append('y')
                continue
            if y==grid_size:
                x += 1
                path.append('x')
                continue
            r = random()
            if r<=.5:
                x += 1
                path.append('x')
            else:
                y += 1
                path.append('y')
        if not(path in possible_paths):
            possible_paths.append(path)
