from globals import NUM_GENERATIONS
from population import Population

def main():
    # creates first population
    population = Population()
    # runs genetic algorithm on however many generations specified
    for _ in range(NUM_GENERATIONS):
        # prints a message for each generation
        population.print_message()
        # creates a new generation
        population.new_generation()
    # gets the best solution after the last generation
    best_solution = population.individuals[0]
    # prints final result
    print(f"~ Generation {population.generation_count} ~\n"
    "====================\n"
    "Fittest Individual\n"
    f"{best_solution}")

if __name__ == "__main__":
    main()