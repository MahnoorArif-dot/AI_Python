
import random
import numpy as np

ITEMS = [(random.randint(1, 10), random.randint(10, 100)) for _ in range(20)] 
WEIGHT_LIMIT = 50
POPULATION_SIZE = 50
GENERATIONS = 200
MUTATION_RATE = 0.1

def fitness_knapsack(chromosome):
    total_weight = sum(ITEMS[i][0] * chromosome[i] for i in range(len(chromosome)))
    total_value = sum(ITEMS[i][1] * chromosome[i] for i in range(len(chromosome)))
    return total_value if total_weight <= WEIGHT_LIMIT else 0

def create_population_knapsack():
    return [[random.randint(0, 1) for _ in range(len(ITEMS))] for _ in range(POPULATION_SIZE)]

def select_parent_knapsack(population, fitness_scores):
    max_score = sum(fitness_scores)
    pick = random.uniform(0, max_score)
    current = 0
    for i, chromosome in enumerate(population):
        current += fitness_scores[i]
        if current >= pick:
            return chromosome

def crossover_knapsack(parent1, parent2):
    point = random.randint(1, len(parent1) - 1)
    return parent1[:point] + parent2[point:]


def mutate_knapsack(chromosome):
    return [gene if random.random() > MUTATION_RATE else 1 - gene for gene in chromosome]

def genetic_algorithm_knapsack():
    population = create_population_knapsack()
    best_solution = None
    best_value = 0

    for generation in range(GENERATIONS):
        fitness_scores = [fitness_knapsack(chromosome) for chromosome in population]
        new_population = []

        for _ in range(POPULATION_SIZE // 2):
            parent1 = select_parent_knapsack(population, fitness_scores)
            parent2 = select_parent_knapsack(population, fitness_scores)
            child1, child2 = crossover_knapsack(parent1, parent2), crossover_knapsack(parent2, parent1)
            new_population.extend([mutate_knapsack(child1), mutate_knapsack(child2)])

        population = new_population

        current_best_solution = max(population, key=lambda x: fitness_knapsack(x))
        current_best_value = fitness_knapsack(current_best_solution)
        if current_best_value > best_value:
            best_value = current_best_value
            best_solution = current_best_solution

        print(f"Generation {generation}: Best Value = {best_value}")

    return best_solution, best_value 

best_solution, best_value = genetic_algorithm_knapsack()
print(f"Best Solution: {best_solution}")
print(f"Best Value: {best_value}")
