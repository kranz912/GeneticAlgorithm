import random
class Individual(object):
    def __init__(self,age):
        self.alleles = None
        self.chromosomes = None
        self.age = 0


    def mutate_genes(self):
        gene = random.choice(self.alleles[0])
        return gene

    def create_gnome(self,length):
        self.chromosomes = [self.mutate_genes() for _ in range(length)]


class Human(Individual):
    def __init__(self,age):
        self.alleles = [['A','C','T'],['X','Y']]
        self.chromosomes = []
        self.age = 0

    def Get_Gender(self):
        if 'Y' in self.chromosomes:
            return 'M'
        else:
            return 'F'

class Male(Human):
    def __init__(self,age):
        self.chromosomes = ['A','A','X','Y']
        self.gender = self.Get_Gender()
        self.age = age

class Female(Human):
    def __init__(self,age):
        self.chromosomes = ['A','A','X','X']
        self.gender = self.Get_Gender()
        self.age = age
