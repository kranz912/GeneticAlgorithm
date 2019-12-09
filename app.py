import random
import constants
from Individual import Individual

GENES = constants.GENES
TARGET = constants.TARGET

POPULATION_SIZE = 100



if __name__ == "__main__":
    
    generation = 1
    found = False

    population = []

    for _ in range(POPULATION_SIZE):
        gnome = Individual.create_gnome(GENES, len(TARGET))
        population.append(Individual(gnome))

    while not found:
        population = sorted(population, key= lambda x:x.fitness)


        if population[0].fitness <= 0:
            found = True
            break

        new_generation = []

        elite_count  = int((10*POPULATION_SIZE)/100)

        new_generation.extend(population[:elite_count])

        
        offspring_count  = int((90*POPULATION_SIZE)/100)

        for _ in range(offspring_count):
            parent1 = random.choice(population[:50])
            parent2 = random.choice(population[:50])

            child = parent1.reproduce(parent2)
            new_generation.append(child)

        population = new_generation

        print("Generation {} \t String: {} \t Fitness: {}".format(generation, "".join(population[0].chromosome),population[0].fitness))
        generation +=1

    
    print("Generation {} \t String: {} \t Fitness: {}".format(generation, "".join(population[0].chromosome),population[0].fitness))