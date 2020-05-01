import sys
import random
import math

OPTIONS = 'a b c d e f g h i j k l m n o p q r s t u v w x y z 0 1 2 3 4 5 6 7 8 9 @'.split()
POPULATION_SIZE = 100
MAX_GENERATION = 200

def get_random_password(size: int) -> str:
    rand_password = ''
    for _ in range(size):
        rand_password += random.choice(OPTIONS)
    return rand_password

# calculate fitness
def score(word:str, pw: str) -> int:
    score = 0
    for word_i, pw_i in zip(word, pw):
        score += (word_i == pw_i)
    return score

def selection(population: list, pw: str) -> tuple:
    fitness = [0 for i in range(POPULATION_SIZE)]
    for idx, element in enumerate(population):
        fitness[idx] = score(element, pw)
    # get the two better ones
    first, second = 0, 0
    m = 0
    for idx, fit in enumerate(fitness):
        if fit > m:
            m = fit
            second = first
            first = idx
    return population[first], population[second]

def crossover(e1: str, e2: str) -> str:
    size = len(e1)
    split_size = math.ceil(size/2)
    elements = (e1, e2)
    x = random.choice([0, 1])
    y = x ^ 1
    return elements[x][:split_size] + elements[y][split_size:]

def mutation(element: str) -> str:
    size = len(element)
    rand_idx = random.choice([i for i in range(size)])
    new_element = ''
    for idx, character in enumerate(element):
        if idx != rand_idx:
            new_element += character
        else:
            new_element += random.choice(OPTIONS)
    return new_element

def have_password(population: list, pw: str) -> bool:
    for element in population:
        if element == pw:
            return True
    return False

if __name__ == '__main__':
    try:
        password = sys.argv[1]
        size = len(password)
        population = [get_random_password(size) for _ in range(POPULATION_SIZE)]
        generation = 0
        find = False
        while not find and generation <= MAX_GENERATION:
            if have_password(population, password):
                find = True
                print("Find password!")
                break
            # generate new population
            e1, e2 = selection(population, password)
            population = [e1, e2]
            for _ in range(POPULATION_SIZE - 2):
                new_element = crossover(e1, e2)
                population.append(mutation(new_element))
            print(f"Generation: {generation}")
            print(f"Best one: '{e1}'")
            generation += 1
    except Exception as e:
        print("Need a password as argument!", e)