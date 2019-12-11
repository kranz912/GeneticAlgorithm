from Individual import Individual 
import random
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


genes  = [0,1,2,3,4,5,6,7,8]
players = []
for x in range(10):
    genome = Player.create_gnome(genes=genes,length=9)
    players.append(Player(genome))





    

#fitness([4, 7, 6, 0, 3, 1, 5, 2, 8])


for x in players:
    print(x.fitness)