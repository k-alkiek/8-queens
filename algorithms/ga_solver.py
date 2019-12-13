import time
from random import randrange, choices, random

from algorithms.abstract_solver import AbstractSolver
from chessboard.chessboard_chromosome import ChessboardChromosome
from chessboard.chessboard_state import ChessboardState
from heapq import heappush, nsmallest

class GASolver(AbstractSolver):

    def __init__(self, n=8, n_population=8, n_generations=10000):
        super(GASolver, self).__init__()
        self.n = n
        self.n_population = n_population
        self.n_generations = n_generations

        self.start_time = 0
        self.end_time = 0
        self.steps = 0
        self.expanded_nodes = 0

    def solve(self):
        self.start_time = time.time()

        population = []
        for i in range(2 * self.n_population):
            chromosome = ChessboardChromosome()
            heappush(population, chromosome)
        population = nsmallest(self.n_population, population)  # Get best n_population elements

        self.expanded_nodes += len(population)

        for i in range(self.n_generations):
            population = self.__crossover_population(population)
            self.__mutate_population(population)
            self.expanded_nodes += len(population)

        best_chromosome = max(population, key=lambda c: c.fitness())
        self.end_time = time.time()
        return best_chromosome.state

    def get_running_time(self):
        return self.end_time - self.start_time

    def get_cost(self):
        return 0

    def get_expanded_count(self):
        return self.expanded_nodes

    def __crossover(self, chromosome_x, chromosome_y):
        sequence_x, sequence_y = chromosome_x.sequence, chromosome_y.sequence
        split_point = randrange(2, len(sequence_x) - 2)

        # building child1
        child1 = [0 for _ in range(self.n)]
        child1[:split_point] = sequence_x[:split_point]
        child1[split_point:] = sequence_y[split_point:]

        # building child2
        child2 = [0 for _ in range(self.n)]
        child2[:split_point] = sequence_y[:split_point]
        child2[split_point:] = sequence_x[split_point:]

        chromosomes = ChessboardChromosome(sequence=child1), ChessboardChromosome(sequence=child2)
        return chromosomes

    def __crossover_population(self, population):
        weights = list(map(lambda c: c.fitness(), population))

        new_population = []
        while len(new_population) < self.n_population:
            chromosome_x = choices(population, weights)[0]
            chromosome_y = choices(population, weights)[0]
            if chromosome_x == chromosome_y:
                continue

            child_1, child_2 = self.__crossover(chromosome_x, chromosome_y)
            new_population.append(child_1)
            new_population.append(child_2)
        return new_population

    def __mutate_population(self, population, probability=0.25):
        for i in range(len(population)):
            if random() < probability:
                sequence = population[i].sequence
                sequence[randrange(self.n)] = randrange(self.n)
                population[i] = ChessboardChromosome(sequence=sequence)


