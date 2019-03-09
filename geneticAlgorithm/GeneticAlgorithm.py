"""
reference : https://towardsdatascience.com/evolution-of-a-salesman-a-complete-genetic-algorithm-tutorial-for-python-6fe5d2b3ca35
"""

import numpy as np, random, operator, pandas as pd, matplotlib.pyplot as plt

class city:
    """
    distance from (x,y)
    """
    def __init__(self, x,y):
        self.x=x
        self.y=y

    def distance(self,city):
        xDis=abs(self.x-city.x)
        yDis=abs(self.y-city.y)

        distance=np.sqrt((xDis**2)+(yDis**2))
        return distance

    def __repr__(self): # instance를 print하면 나오는 string
        return "("+str(self.x)+","+str(self.y)+")"

class Fitness:

    def __init__(self,route):
        self.route=route # route element : city instance
        self.distance=0
        self.fitness=0

    def routeDistance(self):
        if self.distance==0:
            pathDistance=0
            for i in range(0, len(self.route)):
                fromCity=self.route[i]
                toCity=None
                if i+1<len(self.route):
                    toCity=self.route[i+1]
                else: # end of route
                    toCity=self.route[0]
                pathDistance+=fromCity.distance(toCity)
            self.distance=pathDistance
        return self.distance

    def routeFitness(self):
        if self.fitness==0:
            self.fitness=1/float(self.routeDistance())
        return self.fitness



def createRoute(cityList):
    route=random.sample(cityList, len(cityList))
    return route


def initialPopulation(popSize, cityList):
    population=[]
    for i in range(0, popSize):
        population.append(createRoute(cityList))
    return population

def rankRoutes(population):
    fitnessResult={}
    for i in range(len(population)):
        fitnessResult[i]=Fitness(population[i]).routeFitness()

    # key : value
    # value를 기준으로 정렬
    return sorted(fitnessResult.items(), key=operator.itemgetter(1), reverse=True)


class GeneticAlgorithm:

    def __init__(self):
        return None

    def perform(self):
        return None

    def selection(self):
        return None

    def mutation(self):
        return None


    def crossover(self):

        return None
    def substitute(self):
        return None