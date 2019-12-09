def cal_fitness(genome, perfect_genome):
    '''
    Calculate fitness score
    
    '''

    fitness = 0
    for gs, gt  in zip(genome, perfect_genome):
        if gs != gt: fitness +=1
    return fitness
