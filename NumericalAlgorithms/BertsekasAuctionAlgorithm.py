""" implementation of the assignment algorithm described in MTH3330 """
from typing import List


def define_epsilon(n: int):
    """ returns the epsilon for the algorithm, n is the dimension of the matrix """
    return 1/(2*n)


def greedy(matrix: List[List[int]]):
    """ returns the naive-greedy assignment for the cost matrix """
    return [row.index(min(row)) for row in matrix]


def is_one_to_one(x: List[int]) -> bool:
    """ Returns True if x is a one-to-one assignment, False otherwise """
    return min(x) == 0 and max(x) == len(x)-1 == len(set(x))-1


def locate_over_assigned(x: List[int]) -> int:
    """ returns the first instance of a list that appears twice """
    sighted = {}
    for s in x:
        if s in sighted.keys():
            return s
        else:
            sighted[s] = '*'


def assigned_jobs(x: List[int], s: int) -> List[int]:
    """ returns the tasks in x that are assigned to s """
    return [index for index in range(len(x)) if x[index] == s]


def get_second_smallest(task_index, cost_index, cost):
    """ returns the second smallest cost of task i in cost matrix """
    minimum = float('inf')
    for c in cost[task_index]:
        if c < minimum and cost[task_index].index(c) != cost_index:
            minimum = c
    return minimum


def assignment_cost(x: List[int], cost_matrix):
    """ returns the cost of assignment x """
    return sum(cost_matrix[i][x[i]] for i in range(len(x)))


def auction(cost_matrix: List[List[int]]):

    epsilon = define_epsilon(len(cost_matrix))  # returns an ε < 1/n ==> guaranteeing convergence
    cost = cost_matrix

    # first step is to calculate our minimum assignment. We will use the greedy approach.
    premiums = [0 for _ in range(len(cost))]

    while True:
        assignment = greedy(cost)

        # break if assignment is one-to-one
        if is_one_to_one(assignment):
            break

        # otherwise: select a student j that has multiple jobs assigned.
        s = locate_over_assigned(assignment)
        # for all jobs assigned to student:
        deltas = []  # deltas will store our price increases
        for task in assigned_jobs(assignment, s):

            # calculate maximum price increase before assignment changes
            deltas.append([get_second_smallest(task, s, cost_matrix) - cost_matrix[task][s], task])

        # let k be our largest delta and define the minimum bid:
        # j is the job associated with k
        k, j = max(deltas)[0], max(deltas)[1]
        min_bid = k + epsilon

        # we now update our premiums:
        premiums[s] = premiums[s] + min_bid

        # now update column costs:
        for r in range(len(cost)):
            # want to now add premium to all jobs for s except for the one that they are assigned to - j.
            if r != j:
                row = cost[r]
                row[s] += premiums[s]
            else:
                pass

    return assignment


if __name__ == '__main__':
    c = [[8, 7, 15, 12],
         [7, 9, 18, 16],
         [9, 5, 14, 17],
         [6, 10, 11, 15]]

    a = auction(c)
    print(a)

