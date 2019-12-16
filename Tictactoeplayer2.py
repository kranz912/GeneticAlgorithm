from Individual import Individual
import random
import json

genes  = [0,1,2,3,4,5,6,7,8]
population_size = 9*8*7*6*5*4*3*2
players = []


class Player(Individual):
    def __init__(self, chromosome):
        self.chromosome = chromosome

    @classmethod
    def create_gnome(self,length):
        global genes
        genome = []
        for _ in range(length):
            gene =self.mutate_genes(genes)
            while gene in genome:
                gene = self.mutate_genes(genes)
            genome.append(gene)
        return genome


    def reproduce(self,partner):
        global genes
        child_chromosome = []
        gene = None
        for gp1, gp2 in zip(self.chromosome, partner.chromosome):
            while(gene in child_chromosome or gene==None):
                prob = random.random()
                if prob < 0.45:
                    gene = gp1
                elif prob < 0.90:
                    gene = gp2
                else:
                    gene = self.mutate_genes(genes)
                    while gene in child_chromosome:
                        gene = self.mutate_genes(genes)
            child_chromosome.append(gene)
        return Player(child_chromosome)


for _ in range(population_size):

    genome = Player.create_gnome(9)
    players.append(Player(genome))


for player in players:
    print(player.chromosome)


#test_reproduce
child = players[0].reproduce(players[1])
print(child.chromosome)
