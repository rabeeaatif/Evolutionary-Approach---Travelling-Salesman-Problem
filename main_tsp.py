#libraries imported
import random
import numpy as np

# Open input file
infile = open('qa194.tsp', 'r')

# Read instance header
Name = infile.readline().strip().split()[2] # NAME
print("name", Name)
FileType = infile.readline().strip().split()[2] # TYPE
print("FileType", FileType)
Comment = infile.readline().strip().split()[2] # COMMENT
print("Comment", Comment)
Comment = infile.readline().strip().split()[2] # COMMENT
print("Comment", Comment)
Dimension = infile.readline().strip().split()[2] # DIMENSION
print("Dimension", Dimension)
EdgeWeightType = infile.readline().strip().split()[2] # EDGE_WEIGHT_TYPE
print("Dimension", EdgeWeightType)
infile.readline()

# Read node list
dist_list = []
N = int(Dimension)
for i in range(0, int(Dimension)):
    x,y = infile.readline().strip().split()[1:]
    dist_list.append([float(x), float(y)])

# Close input file
infile.close()

"""
Selection schemes:
1. Truncation
2. Fitness
"""
def cumulative(lists): 
    cu_list = [] 
    length = len(lists) 
    cu_list = [sum(lists[0:x:1]) for x in range(0, length+1)] 
    print("cumulative list", cu_list)
    return cu_list[1:]

def fps(fit):
    new_parents = []
    hist_list = []
    hist_list = cumulative(fit)
    f = fit[0]
    h = hist_list[-1]
    # print(type(fit))

    # print(h)
    # print(f)
    for i in range(2):
        r =  random.randint(int(fit[0]),int(hist_list[-1]))
        print("random number", r)
        k = len(hist_list)-1
    

        while (k!= -1):
            if ( r < hist_list[k] and r >  hist_list[k-1]):
                print("k", k)
                parent_fitness = fit[k]
                parent = population[k]
                new_parents.append(k)
                break
            k = k - 1
        print("parenT", parent,"parentfitness", parent_fitness)
    print(new_parents)
    return new_parents

def post_parent_selection():
    children = []

    mutation()
    crossover





print(dist_list)


"""
1. Create a random population of 50 different routes/chromosomes
2. Find the distance of each chromosome and pathlenght
3. This is the fitness
4. 
"""
city_arr = []
population = []
size = 30

def create_citylist(arr):
    for i in range(1,int(Dimension) + 1):
        arr.append(i)

def init_pop(population, s):
    path = []
    while (s != 0):
        path = random.sample(city_arr, int(Dimension))
        population.append(path)
        s = s - 1

def path_distance(path):
    total_path_len = 0
    d = 0
    #[93, 50, 96, 85, 115, 68, 84, 152, 77, 73, 162, 101, 26, 133, 25, 53, 141, 188, 18, 157, 150, 124, 144, 178, 183, 33, 119, 22, 131, 191, 11, 190, 126, 120, 166, 176, 23, 32, 160, 194, 149, 71, 13, 180, 174, 28, 83, 143, 134, 45, 91, 38, 12, 146, 75, 35, 49, 61, 90, 29, 155, 172, 165, 8, 43, 16, 105, 76, 59, 46, 57, 121, 179, 113, 7, 78, 9, 123, 48, 67, 137, 132, 158, 153, 148, 184, 30, 42, 20, 112, 173, 36, 69, 92, 86, 177, 95, 186, 66, 135, 5, 181, 156, 55, 170, 192, 122, 110, 54, 130, 109, 79, 163, 129, 52, 60, 193, 175, 
#161, 185, 21, 24, 106, 27, 2, 4, 125, 140, 64, 154, 1, 114, 182, 81, 159, 72, 139, 40, 41, 19, 168, 97, 136, 89, 116, 187, 102, 17, 56, 39, 3, 51, 65, 117, 138, 145, 147, 127, 111, 62, 15, 58, 99, 100, 108, 47, 151, 107, 14, 74, 6, 44, 128, 82, 88, 80, 142, 10, 171, 103, 31, 37, 70, 118, 94, 87, 189, 63, 164, 167, 169, 34, 98, 104]
    
    for i in range(len(path)-1):
        x_dist = abs(dist_list[path[i]-1][0] - dist_list[path[i+1]-1][0])
        y_dist = abs(dist_list[path[i]-1][1] - dist_list[path[i+1]-1][1])
        d = np.sqrt((x_dist ** 2) + (y_dist ** 2))
        total_path_len += d
    print("total_path_len", total_path_len)
    return total_path_len

def path_fitness(population):
    fitness_arr =[]
    for x in population:
        print("x", x)
        dist = path_distance(x)
        print("distanceee", dist)
        fitness_arr.append(dist)
    return fitness_arr


fit = []
create_citylist(city_arr)
init_pop(population, size)
print(city_arr)
print(population)
fit = path_fitness(population)
print("fitness array", fit)
print("fit parent", fps(fit))
