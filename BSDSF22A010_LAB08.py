import random

def initialize_population(pop_size, string_length):
    return [''.join(random.choice('01') for _ in range(string_length)) for _ in range(pop_size)]

def calculate_fitness(individual):
    return individual.count('1')

def select_parents(population, fitness_scores):
    total_fitness = sum(fitness_scores)
    probabilities = [score / total_fitness for score in fitness_scores]
    parent1 = random.choices(population, weights=probabilities, k=1)[0]
    parent2 = random.choices(population, weights=probabilities, k=1)[0]
    return parent1, parent2

def crossover(parent1, parent2):
    point = random.randint(1, len(parent1) - 1)
    offspring = parent1[:point] + parent2[point:]
    return offspring

def mutate(individual, mutation_rate):
    individual = list(individual)
    for i in range(len(individual)):
        if random.random() < mutation_rate:
            individual[i] = '1' if individual[i] == '0' else '0'
    return ''.join(individual)

def genetic_algorithm(string_length, pop_size, num_generations, mutation_rate):
    population = initialize_population(pop_size, string_length)
    for generation in range(num_generations):
        fitness_scores = [calculate_fitness(individual) for individual in population]
        best_individual = population[fitness_scores.index(max(fitness_scores))]
        best_fitness = max(fitness_scores)
        print(f"Generation {generation}: Best Fitness = {best_fitness}, Best Individual = {best_individual}")
        new_population = []
        for _ in range(pop_size):
            parent1, parent2 = select_parents(population, fitness_scores)
            offspring = crossover(parent1, parent2)
            offspring = mutate(offspring, mutation_rate)
            new_population.append(offspring)
        population = new_population
    return best_individual, best_fitness

if __name__ == "__main__":
    string_length = 20
    pop_size = 50
    num_generations = 100
    mutation_rate = 0.05
    best_solution, best_fitness = genetic_algorithm(string_length, pop_size, num_generations, mutation_rate)
    print("\nOptimal Solution:", best_solution)
    print("Optimal Fitness:", best_fitness)
