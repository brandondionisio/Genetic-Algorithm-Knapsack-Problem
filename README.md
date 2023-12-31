# Genetic-Algorithm-Knapsack-Problem

Implementation of a genetic algorithm to solve the Knapsack Problem -- that is, find the optimal unique boxes to put in a knapsack to obtain the greatest value without going over the maximum weight.

## Title

CS 131 HW 03 - The Knapsack Problem

## Author

Brandon Dionisio

## Boxes

![image](https://github.com/brandondionisio/Genetic-Algorithm-Knapsack-Problem/assets/145251710/7178b055-25dc-4ed6-b80e-9d5f1b37bf97)

This list represents the complete set of boxes: for each, the top value indicates the weight (higher means heavier); the bottom value represents the importance (higher means more important).

## Acknowledgements

stackoverflow  
CS 131 Canvas Slides  
CS 131 Piazza  
docs.python.org

## Running The Program

To run the genetic algorithm, use "python3 run.py"  
Change global variables to alter aspects of the genetic algorithm

## Global Variables

NUM_GENERATIONS - Maximum number of generations the algorithm will run (>= 1 & integer)  
NUM_POPULATION -  Number of individuals in the population (> 1 & integer)  
MUTATION_RATE - Probability of an individual having a single-point mutation (0 <= mutation_rate <= 1)  
CULL_RATE - Percentage of population that remains for future generations (>= 0.01)  
MAX_WEIGHT - Maximum weight that an individual can be (max weight in the backpack) (>= 20 & integer)

## Assumptions

Offsprings are created with one-point crossovers and a potential single-point mutation based on MUTATION_RATE

Fitness function returns the total value of the genotype for the individual if boxes are not overweight and returns 0 if boxes are overweight

Only uses the given set of unique boxes without duplicates
