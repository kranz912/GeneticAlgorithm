from Individual import Individual
import random
import json

genes  = [0,1,2,3,4,5,6,7,8]
population_size = 400


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






def savegenetictree(tree,players,generation):
    tree[generation] = []
    X_wins = 0
    O_wins = 0
    Draws = 0
    for x in players:
        tree[generation].append({"chromosome":x.chromosome,"fitness":x.fitness})
        if x.fitness == 3:
            X_wins += 1
        elif x.fitness == -3:
            O_wins +=1
        else:
            Draws +=1
    #tree[generation]['X_wins'] = X_wins
    #tree[generation]['O_wins'] = O_wins
    #tree[generation]['Draws'] = Draws
    with open('result.json','w+') as output:
        json.dump(tree,output)
    return tree



#fitness([4, 7, 6, 0, 3, 1, 5, 2, 8])
tree = {}
for _ in range(1000):

    players = sorted(players, key= lambda x:x.fitness)

    print('Generation: {}'.format(_+1))

    savegenetictree(tree,players,_+1)

    new_generation = []
    elite_count =  int((10*population_size)/100)

    new_generation.extend(players[:elite_count])

    offspring_count= int((90*population_size)/100)

    for __ in range(offspring_count):
        parent1 = random.choice(players[:200])
        parent2 = random.choice(players[:200])

        child = parent1.reproduce(parent2)

        new_generation.append(child)
    players = new_generation


players = sorted(players, key= lambda x:x.fitness)

model = {}

model['moves'] =[]

O_wins = 0
X_wins = 0

for x in players:
    winner = 'draw'
    if x.fitness == 3:
        winner = 'X'
        X_wins +=1
    elif x.fitness == -3:
        winner = 'O'
        O_wins += 1
    print("moves: {}  winner: {}".format(x.chromosome,winner))
    model['moves'].append(x.chromosome)

draws = population_size -(X_wins+O_wins)
print('X:{} O:{} draws {}'.format(X_wins,O_wins, draws))
with open('model.json','w') as output:
    json.dump(model,output)
