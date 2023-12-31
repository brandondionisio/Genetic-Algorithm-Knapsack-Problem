from globals import CULL_RATE, NUM_POPULATION
from genotype import Genotype

class Population:

    # constructor for population class
    # sets the generation count to 0 and creates list of randomly generated
    # genotypes equal to the population number
    def __init__(self):
        self.generation_count = 0
        self.individuals = []
        for _ in range(NUM_POPULATION):
            self.individuals.append(Genotype())

    # fitness function for genetic algorithm
    # returns the total value of the genotype for the individual if boxes are not overweight
    # returns 0 if boxes are overweight
    def fitness(self, individual):
        if not individual.isOverweight():
            return individual.getValue()
        return 0

    # creates a new generation of individuals for the population
    def new_generation(self):
        # culls the top individuals of the population according to the cull rate (individuals are sorted).
        self.individuals = self.individuals[:int(NUM_POPULATION * CULL_RATE)]
        # reproduces from the culled individuals
        new_individuals = []
        for i in range(0, len(self.individuals), 2):
            parent_1 = self.individuals[i]
            if i + 1 < len(self.individuals):
                parent_2 = self.individuals[i + 1]
                new_individuals.append(parent_1.reproduce(parent_2))
        # adds the reproduced individuals to the culled individuals, creating the new population
        self.individuals.extend(new_individuals)
        # resorts the new population
        self.individuals.sort(key=self.fitness, reverse=True)
        # increases the generation count
        self.generation_count += 1

    # prints a message describing the population
    def print_message(self):
        best_individual = self.individuals[0]
        weight_list = [individual.getWeight() for individual in self.individuals]
        value_list = [individual.getValue() for individual in self.individuals]
        avg_value = sum(value_list) / NUM_POPULATION
        avg_weight = sum(weight_list) / NUM_POPULATION
        print(f"~ Generation {self.generation_count} ~\n"
        "====================\n"
        f"Average Value: {avg_value}\n"
        f"Average Weight: {avg_weight}\n"
        f"Best Value: {best_individual.getValue()}\n")