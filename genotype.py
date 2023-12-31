import random
from globals import MAX_WEIGHT, MUTATION_RATE

# data is a list of dictionaries that represents each unique box
# each box contains a weight and a value.
data = [
        {"weight": 20, "value": 6},
        {"weight": 30, "value": 5},
        {"weight": 60, "value": 8},
        {"weight": 90, "value": 7},
        {"weight": 50, "value": 6},
        {"weight": 70, "value": 9},
        {"weight": 30, "value": 4},
        {"weight": 30, "value": 5},
        {"weight": 70, "value": 4},
        {"weight": 20, "value": 9},
        {"weight": 20, "value": 2},
        {"weight": 60, "value": 1}
    ]

class Genotype:

    # constructor that sets the genotype's information, represented as a list of 0's and 1's
    # sets the information if given or randomizes it if not
    def __init__(self, genotype_info=None):
        self.genotype_info = genotype_info
        if genotype_info is None:
            self.genotype_info = [bool(random.getrandbits(1)) for _ in data]

    # returns a string representation of the genotype
    def __str__(self):
        msg = f"Value: {self.getValue()}\n"
        msg += f"Total Weight: {self.getWeight()}\n"
        msg += f"- Boxes -\n"
        for (i, genotype_info) in enumerate(self.genotype_info):
            if genotype_info:
                msg += f"Box #: {str(i + 1)}, Value: {data[i]['value']}, Weight: {data[i]['weight']}\n"
        return msg

    # returns the total value of the boxes of the genotype
    def getValue(self):
        total_value = 0
        for i, selected in enumerate(self.genotype_info):
            if selected:
                total_value += data[i]["value"]
        return total_value

    # returns the total weight of the boxes of the genotype
    def getWeight(self):
        total_weight = 0
        for i, selected in enumerate(self.genotype_info):
            if selected:
                total_weight += data[i]["weight"]
        return total_weight

    # returns true if the total weight of the boxes in the genotype is over the maximum weight; false if not
    def isOverweight(self):
        return self.getWeight() > MAX_WEIGHT
    
    # creates an offspring with two given genotypes
    # first, crosses the two genotypes; then, potentially performs a mutation
    # returns the offspring genotype
    def reproduce(self, other):
        # performs a one-point crossover on two genotypes, swapping if the boxes exist around a random point
        i = random.randint(0, len(self.genotype_info) - 1)
        offspring = Genotype(self.genotype_info[:i] + other.genotype_info[i:])

        # performs a single-point mutation on the genotype, negating if a random box exists
        if (random.random() > MUTATION_RATE):
            i = random.randint(0, len(offspring.genotype_info) - 1)
            offspring.genotype_info[i] = not offspring.genotype_info[i]
        return offspring