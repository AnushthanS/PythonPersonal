import random
import math

p = int(input("Enter value of p: "))
c = int(input("Enter value of c: "))
m = int(input("Enter value of m: "))
t = int(input("Enter value of t: "))
x = int(input("Enter value of x: "))
i = int(input("Enter value of i: "))

population = []
binary_population = []
mutated = []
mutated_decimal = []
offsprings = []
improvement_flag = 0
t_count = 0
i_count = 0


def decToBin(num):
    if(num == 0): return '00000'
    str = "{0:b}".format(int(num))

    k = 5 - len(str)
    temp = ""
    for index in range (0, k):
        temp += "0"
    
    str = temp + str
    return str



def fitness(population):
    fitness_sum = 0;
    for key in population:
        fitness_sum += key*key
    return fitness_sum



def randomPool(population, p):
    for index in range(p):
        population.append(math.floor(random.uniform(0, 32)))



def makeBinaryPool(population):
    for index in range(0, len(population)):
        binary_population.append(decToBin(population[index]))



def genetic():
    fitness_sum = fitness(population)
    parents = []
    for index in range(len(population)):
        probability = (population[index]*population[index])/fitness_sum
        count = round(probability * p)
        while (count > 0 and len(binary_population) <= len(population)):
            parents.append(binary_population[index])
            count -= 1

    point = 0
    if(c == 0): point = 1
    else: point = 2

    size = len(parents)
    
    index = 0
    while(index < size - 1):
        p1 = parents[index]
        p2 = parents[index + 1]
        index += 2

        m1 = p1[:point]
        n1 = p1[point:]
        a = p2[:point]
        b = p2[point:]
        off1 = m1 + b
        off2 = a + n1
        offsprings.append(off1)
        offsprings.append(off2)

    if(m == 0):
        for index in range(0, len(offsprings)):
            moff = offsprings[index]
            lbit = moff[4]
            if(lbit == '1'): lbit = '0'
            else: lbit = '1'
            moff = moff[:4] + lbit
            mutated.append(moff)

    if(m == 1):
        for index in range(0, len(offsprings)):
            str = offsprings[index]
            lst = []
            for letter in str:
                lst.append(letter)
            for j in range (0, 2):
                temp = lst[j]
                lst[j] = lst[4-j]
                lst[4-j] = temp
            
            moff = ""
            for key in lst:
                moff += key

            mutated.append(moff)

    for index in range(0, len(mutated)):
        mutated_decimal.append(int(mutated[index],2))

    new_fitness = fitness(mutated_decimal)
    if(new_fitness > fitness_sum): improvement_flag = 1

for iterations in range(0, i):
    i_count += 1
    if(iterations == 0):
        randomPool(population, p)
        makeBinaryPool(population)
        genetic()
        continue

    if(t == 0):
        if(improvement_flag == 0): t_count += 1
        if(t_count == x): 
            print(f"stopped after {i_count} iterations")
            break
    
    population = mutated_decimal
    binary_population = mutated
    mutated = []
    offsprings = []
    mutated_decimal = []
    improvement_flag = 0
    genetic()


print(max(mutated_decimal))