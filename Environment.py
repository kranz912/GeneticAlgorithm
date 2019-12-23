from Humans import Male,Female,Human
import random
import json
from Helper import Encoder
class Environment(object):
    def __init__(self,NGEN,generation_length):
        self.population = []

        self.period = generation_length
        self.NGEN = NGEN

    def reproduce(self,parent1,parent2):
        child = Human(0)

        for gp1, gp2  in zip(parent1.chromosomes[:-2], parent2.chromosomes[:-2]):
            prob = random.random()
            if prob < 0.45:
                child.chromosomes.append(gp1)
            elif prob <0.90:
                child.chromosomes.append(gp2)
            else:
                child.chromosomes.append(child.mutate_genes())

        child.chromosomes.append('X')

        prob = random.random()
        if prob < 0.50:
            child.chromosomes.append('X')
            offspring = Female(0)
        else:
            child.chromosomes.append('Y')
            offspring = Male(0)

        offspring.chromosomes = child.chromosomes



        return offspring


    def update_age(self):
        for x in self.population:
            x.age += 1

    def run(self):
        Adam = Male(20)

        Eve = Female(20)
        self.generation = {}
        self.population.append(Adam)
        self.population.append(Eve)

        self.generation['Gen0'] = self.population


        for gen in range(self.NGEN):
            for years in range(self.period):
                prob = random.random()
                if prob < 0.10:
                    male = random.choice([x for x in self.population if x.gender =='M'])
                    female = random.choice([x for x in self.population if x.gender =='F'])
                    child = self.reproduce(male,female)
                    self.population.append(child)
                self.update_age()
            self.generation['Gen{}'.format(gen)] = self.population
        print(self.generation)
        self.js = Encoder().encode(self.generation)
        with open('gen.json','w+') as output:
            json.dump(self.js,output)


Environment(10,30).run()
