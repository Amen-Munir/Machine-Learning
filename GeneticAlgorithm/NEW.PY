import random

class Gene:
    def __init__(self, gene: str = "", fitness: int = 0, fitnessRatio: float = 0.0, commualativeFitness: float = 0.0):
        self.gene = gene
        self.fitness = fitness
        self.fitnessRatio = fitnessRatio
        self.commualativeFitness = commualativeFitness

    def __repr__(self):
        return f"Gene(gene='{self.gene}', fitness={self.fitness}, fitnessRatio={self.fitnessRatio}, commualativeFitness={self.commualativeFitness})"

populationSize = 10
lengthOfEachString = 8


def generatePop():
    population = []
    for _ in range(populationSize):
        gene_string = ''.join(random.choice(['0', '1']) for _ in range(lengthOfEachString))
        population.append(Gene(gene=gene_string))
    return population


def fitnessFunction(population):
    for individual in population:
        individual.fitness = individual.gene.count('1')
    return population



def rankPop(population):
    return sorted(population, key=lambda x: x.fitness, reverse=True)


def calculateFitnessRatio(population):
    totalFitness = sum(individual.fitness for individual in population)
    for individual in population:
        individual.fitnessRatio = round(individual.fitness / totalFitness, 3) * 100
    return population


def calculateCumulativeFitness(population):
    cumulative = 0
    for individual in population:
        cumulative += individual.fitnessRatio
        individual.commualativeFitness = cumulative
    return population



def rouletteWheelSelection(population):
    r = random.uniform(0, 100)  
    print(f"Random Number: {r}")
    for individual in population:
        if r <= individual.commualativeFitness:
            return individual

def crossover(parent1,parent2):
    r = int(random.uniform(0,8) )
    print(f"Random Number: {r}")
    child1=parent1.gene[:r]+parent2.gene[r:]
    child2=parent2.gene[:r]+parent1.gene[r:]
    return child1,child2



def mutation(c1):
    r = random.randint(0, lengthOfEachString - 1)
    c1 = list(c1)  
    c1[r] = '0' if c1[r] == '1' else '1'
    return ''.join(c1)  


Population = generatePop()
Population = fitnessFunction(Population)
Population = rankPop(Population)
Population = calculateFitnessRatio(Population)
Population = calculateCumulativeFitness(Population)


for i in range(populationSize):
    print("-----------------------")
    print(Population[i])


parent1 = rouletteWheelSelection(Population)
parent2=rouletteWheelSelection(Population)
print("\nSelected Parent:")
print(parent1)
print(parent2)
c1,c2=crossover(parent1,parent2)
print(f"\nChild 1: {c1}")
print(f"\nChild 2: {c2}")
c1=mutation(c1)
c2=mutation(c2)
print(f"\nMutated Child 1: {c1}")
print(f"\nMutated Child 2: {c2}")