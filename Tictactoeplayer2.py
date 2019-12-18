from Individual import Individual
import random
import json
import math
genes  = [0,1,2,3,4,5,6,7,8]
population_size = 200000
players = []


class Player(Individual):
    def __init__(self, chromosome):
        self.chromosome = chromosome

        self.count = self.Count()
        self.score = self.Score()

        self.fitness = self.count * self.score


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



    def Count(self):
        global players
        count = 1
        for player in players:
            if player.chromosome == self.chromosome:
                count += 1
        return count


    def Score(self):
        board = [0,0,0,0,0,0,0,0,0]
        win = [
                [0,1,2],
                [3,4,5],
                [6,7,8],
                [0,3,6],
                [1,4,7],
                [2,5,8],
                [0,4,8],
                [2,4,6]
                ]
        turn = 'X'
        winner = ''
        for c in self.chromosome:
            if turn == 'X':
                board[c] =1
                turn = 'O'
            else:
                board[c] =-1
                turn ='X'
            for w in win:
                score = 0
                for e in w:
                    score += board[e]
                    if score == 3:
                        return score
                    elif score == -3:
                        return score
        return 0




for _ in range(population_size):
    genome = Player.create_gnome(9)
    players.append(Player(genome))


generation = 1
while True:

    print("Generation: {}".format(generation))
    new_generation = list(filter(lambda x:x.count==1 and x.fitness<=0,players))

    duplicates = list(filter(lambda x:x.count!=1, players))
    players = sorted(players, key= lambda x:x.fitness)
    if len(duplicates)==0:
        break

    for _ in range(len(duplicates)):
        elites = math.floor(len(players)/2)
        print(elites)
        parent1 = random.choice(players[:elites])
        parent2 = random.choice(players[:elites])

        child = parent1.reproduce(parent2)
        new_generation.append(child)
    players = new_generation
    generation +=1

duplicates = list(filter(lambda x:x.count!=1, players))
for dup in duplicates:
    print(dup.chromosome)

#
for player in players:
    print('genome:{} fitness:{}'.format(player.chromosome,player.fitness))
