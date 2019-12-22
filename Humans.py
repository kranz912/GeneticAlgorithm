import random
class Individual(object):
    def __init__(self):
        self.alleles = None
        self.chromosomes = None


    def mutate_genes(self):
        gene = random.choice(self.alleles[-1])
        return gene

    def create_gnome(self,length):
        self.chromosomes = [self.mutate_genes() for _ in range(length)]


class Human(Individual):
    def __init__(self):
        self.alleles = [['X','Y']]

    def Get_Gender(self):
        if 'Y' in self.chromosomes:
            return 'M'
        else:
            return 'Y'

class Male(Human):
    def __init__(self):
        self.chromosomes = ['X','Y']
        self.gender = self.Get_Gender()

class Female(Human):
    def __init__(self):
        self.chromosomes = ['X','X']
        self.gender = self.Get_Gender()
