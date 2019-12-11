import random
import constants
import Fitness
class Individual(object):
    def __init__(self, chromosome):
        self.chromosome = chromosome
        self.fitness = Fitness.cal_fitness(chromosome,constants.TARGET)
   
   
    @classmethod
    def mutate_genes(self,genes):
        gene = random.choice(genes)
        return gene

    @classmethod
    def create_gnome(self,genes,length):
        return [self.mutate_genes(genes) for _ in range(length)]
    
    def reproduce(self, partner):
        child_chromosome = []
        for gp1, gp2 in zip(self.chromosome, partner.chromosome):
            prob = random.random()

            if prob < 0.45:
                child_chromosome.append(gp1)
            
            elif prob < 0.90:
                child_chromosome.append(gp2)
            
            else:
                '''
                    small chance that a mutation will occur
                '''
                child_chromosome.append(self.mutate_genes(constants.GENES))
        return Individual(child_chromosome)
    
