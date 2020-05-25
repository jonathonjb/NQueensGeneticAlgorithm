from NQueens import NQueens
import copy
import random

class GeneticAlgorithm():
    def __init__(self, populationNum, object, fitnessFunction):
        self.object = object
        self.population = []
        self.initPopulation(populationNum, object)
        self.fitnessFunction = fitnessFunction

    def initPopulation(self, populationNum, object):
        for i in range(populationNum):
            self.population.append(object())


    def evolve(self, numOfEvolutionaryCycles, probabilityThreshold, mutationProbability = 0.015):
        for i in range(numOfEvolutionaryCycles):
            pairs = self.select(probabilityThreshold)
            self.cross(pairs)
            self.mutate(mutationProbability)

    def select(self, probabilityThreshold):
        fitnessValues = list(map(self.fitnessFunction, self.population))
        fitnessValueMap = {}
        for i in range(len(fitnessValues)):
            fitnessValueMap[self.population[i]] = fitnessValues[i]

        fitnessValues.sort()

        thresholdNum = int(len(self.population) * probabilityThreshold)
        worstFitnessValueThreshold = fitnessValues[thresholdNum - 1]
        duplicateFitnessValueThreshold = fitnessValues[len(fitnessValues) - thresholdNum]

        while(worstFitnessValueThreshold >= duplicateFitnessValueThreshold and
              (fitnessValues[0] != fitnessValues[len(fitnessValues) - 1])):
            thresholdNum -= 1
            worstFitnessValueThreshold = fitnessValues[thresholdNum - 1]
            duplicateFitnessValueThreshold = fitnessValues[len(fitnessValues) - thresholdNum]

        # removes the worst N% of the population
        numRemoved = 0
        i = 0
        while(numRemoved < thresholdNum):
            fitnessValue = fitnessValueMap.get(self.population[i])
            if(fitnessValue <= worstFitnessValueThreshold):
                self.population.pop(i)
                numRemoved += 1
                i -= 1
            i += 1

        # duplicates the best N% of the population
        numDuplicated = 0
        i = 0
        while(numDuplicated < thresholdNum):
            fitnessValue = fitnessValueMap.get(self.population[i])
            if (fitnessValue >= duplicateFitnessValueThreshold):
                object = self.population[i]
                self.population.insert(0, copy.deepcopy(object))
                numDuplicated += 1
                i += 1
            i += 1

        # selects the pairs
        pairs = []
        while(len(self.population) > 0):
            indexOne = random.randint(0, len(self.population) - 1)
            indexTwo = random.randint(0, len(self.population) - 1)
            if(indexOne == indexTwo):
                continue
            pair = [self.population.pop(indexOne), self.population.pop(indexTwo - 1)]
            pairs.append(pair)
        self.population = []
        return pairs


    def cross(self, pairs):
        for pair in pairs:
            pairOneAttributes = pair[0].getAttributes()
            pairTwoAttributes = pair[1].getAttributes()

            numOfAttributes = len(pairOneAttributes)
            splitIndex = random.randint(1, numOfAttributes - 2)

            childOneAttributes = pairOneAttributes[:splitIndex] + pairTwoAttributes[splitIndex:]
            childOne = self.object(numOfAttributes, childOneAttributes)
            self.population.append(childOne)

            childTwoAttributes = pairTwoAttributes[:splitIndex] + pairOneAttributes[splitIndex:]
            childTwo = self.object(numOfAttributes, childTwoAttributes)
            self.population.append(childTwo)

    def mutate(self, mutationProbability):
        for i in range(len(self.population)):
            if(random.uniform(0, 1) <= mutationProbability):
                self.population[i].changeOneValue()

    def printPopulation(self):
        for i in range(len(self.population)):
            print(self.population[i])
        print("\n\n")

def main():
    geneticAlgorithm = GeneticAlgorithm(100, NQueens, NQueens.fitnessFunction)
    geneticAlgorithm.evolve(500, .05)
    geneticAlgorithm.printPopulation()

if __name__ == '__main__':
    main()