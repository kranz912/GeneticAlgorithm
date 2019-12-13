from Individual import Individual
import random


genes  = [0,1,2,3,4,5,6,7,8]
population_size = 10


class Player(Individual):

    def __init__(self,chromosome):
        self.chromosome = chromosome
        self.fitness = self.Fitness()

    @classmethod
    def create_gnome(self,genes,length):
        genome = []
        for _ in range(length):
            gene = self.mutate_genes(genes)
            while gene in genome:
                gene =self.mutate_genes(genes)
            genome.append(gene)
        return genome

    def reproduce(self,partner):
        child_chromosome = []
        global genes
        gene = self.mutate_genes(genes)
        for gp1, gp2 in zip(self.chromosome, partner.chromosome):

            while(gene in child_chromosome):
                prob = random.random()
                if prob < 0.45:
                    gene=gp1
                elif prob < 0.90:
                    gene=gp2
                else:
                    gene = self.mutate_genes(genes)
                    while gene in child_chromosome:
                        gene = self.mutate_genes(genes)

            child_chromosome.append(gene)
        return Player(child_chromosome)

    def Fitness(self):
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



players = []
for x in range(population_size):
    genome = Player.create_gnome(genes=genes,length=9)
    players.append(Player(genome))



#fitness([4, 7, 6, 0, 3, 1, 5, 2, 8])
for _ in range(10000):

    players = sorted(players, key= lambda x:x.fitness)

    print('Generation: {}'.format(_+1))
    for x in players:
        winner = 'draw'
        if x.fitness == 3:
            winner = 'X'
        elif x.fitness == -3:
            winner = 'O'
        print("moves: {}  winner: {}".format(x.chromosome,winner))


    new_generation = []
    elite_count =  int((10*population_size)/100)

    new_generation.extend(players[:elite_count])

    offspring_count= int((90*population_size)/100)

    for __ in range(offspring_count):
        parent1 = random.choice(players[:50])
        parent2 = random.choice(players[:50])

        child = parent1.reproduce(parent2)

        new_generation.append(child)
    players = new_generation
