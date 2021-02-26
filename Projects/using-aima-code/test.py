from abc import ABC

from search import *
from utils import *

import sys
import click

"""
Ziad:

I redefined each of the search algorithms to return a tuple with the results
and the number of expansions (result, expansions)
"""


def breadth_first_tree_search(problem):
    """
    [Figure 3.7]
    Search the shallowest nodes in the search tree first.
    Search through the successors of a problem to find a goal.
    The argument frontier should be an empty queue.
    Repeats infinitely in case of loops.
    """
    expansions = 0

    frontier = deque([Node(problem.initial)])  # FIFO queue

    while frontier:
        node = frontier.popleft()
        expansions += 1
        if problem.goal_test(node.state):
            return node, expansions
        frontier.extend(node.expand(problem))
    return None, expansions


def depth_first_tree_search(problem):
    """
    [Figure 3.7]
    Search the deepest nodes in the search tree first.
    Search through the successors of a problem to find a goal.
    The argument frontier should be an empty queue.
    Repeats infinitely in case of loops.
    """

    expansions = 0

    frontier = [Node(problem.initial)]  # Stack

    while frontier:
        node = frontier.pop()
        expansions += 1
        if problem.goal_test(node.state):
            return node, expansions
        frontier.extend(node.expand(problem))

    return None, expansions


def depth_limited_search(problem, limit=50, expansions=0):
    """[Figure 3.17]"""

    def recursive_dls(node, problem, limit, expansions):
        if problem.goal_test(node.state):
            return node, expansions
        elif limit == 0:
            return 'cutoff', expansions
        else:
            cutoff_occurred = False
            for child in node.expand(problem):
                expansions += 1
                result = recursive_dls(child, problem, limit - 1,
                                       expansions)
                if result[0] == 'cutoff':
                    cutoff_occurred = True
                elif result[0] is not None:
                    return result
            return ('cutoff', expansions) if cutoff_occurred else (
                None, expansions)

    # Body of depth_limited_search:
    return recursive_dls(Node(problem.initial), problem, limit, 0)


def iterative_deepening_search(problem):
    """[Figure 3.18]"""

    """
    Ziad:
    
    I combined the expansions count from all the DLS calls
    """
    expansions = 0
    for depth in range(sys.maxsize):
        result = depth_limited_search(problem, depth)
        expansions = expansions + result[1]
        if result[0] != 'cutoff':
            return result[0], expansions


def conflict(row1, col1, row2, col2):
    """Would putting two queens in (row1, col1) and (row2, col2) conflict?"""
    return (row1 == row2 or  # same row
            col1 == col2 or  # same column
            row1 - col1 == row2 - col2 or  # same \ diagonal
            row1 + col1 == row2 + col2)  # same / diagonal


def conflicted(state, row, col):
    """Would placing a queen at (row, col) conflict with anything?"""
    return any(conflict(row, col, state[c], c)
               for c in range(col))


def h(node):
    """Return number of conflicting queens for a given node"""
    num_conflicts = 0
    for (r1, c1) in enumerate(node.state):
        for (r2, c2) in enumerate(node.state):
            if (r1, c1) != (r2, c2):
                num_conflicts += conflict(r1, c1, r2, c2)

    return num_conflicts


def number_of_conflicting_pairs(state):
    """
    Ziad:

    I modified the h() function to accept the state instead of the node,
    and divide the result by two so we have pairs instead of individual
    cases
    """
    num_conflicts = 0
    for (r1, c1) in enumerate(state):
        for (r2, c2) in enumerate(state):
            if (r1, c1) != (r2, c2):
                num_conflicts += conflict(r1, c1, r2, c2)
    return num_conflicts / 2


class NQueensDefectedProblem(Problem, ABC):
    """
    Ziad:

    This is a modified version of NQueensProblem from search.py which changes
    the goal_test() to make use of the h() function and count how many
    conflicting queens there are.
    """

    def __init__(self, n, k):
        super().__init__(tuple([-1] * n))
        self.N = n
        self.K = k

    def actions(self, state):
        """In the leftmost empty column, try all non-conflicting rows."""
        if state[-1] != -1:
            return []  # All columns filled; no successors
        else:
            """
            Ziad:
            modified the rows generator to try all possible rows not just
            non-conflicting rows
            """
            return [row for row in range(self.N)]

    def result(self, state, row):
        """Place the next queen at the given row."""
        col = state.index(-1)
        new = list(state[:])
        new[col] = row
        return tuple(new)

    def goal_test(self, state):
        """Check if all columns filled, no conflicts."""

        if state[-1] == -1:
            return False
        # return any(self.conflicted(state, state[col], col)
        #                for col in range(len(state))
        """
        Ziad:
        
        Instead of checking if there are any conflicts we check
        if the count of conflicting pairs matches the input K value
        """

        return (number_of_conflicting_pairs(state)) == self.K


# extreme test cases
# def pairs(x, y):
#     for i in range(1, x):
#         for j in range(1, y):
#             yield i, j

# test_inputs = [(x, y) for x, y in pairs(8, 8)]

print("You can enter a list of pairs of inputs separated by spaces")
print()
print("for example:")
print("python3 test.py 1,2 3,4 5,6")
print("will run the searches on n=1,k=2 n=3,k=4 n=5,k=6")
print("if no input is given it will use my default list of inputs")
print(f"Arguments count: {len(sys.argv)}")
for i, arg in enumerate(sys.argv):
    print(f"Argument {i:>6}: {arg}")

test_inputs = []
# 35 Random Test cases
# test_inputs = [(7, 3), (4, 7), (5, 6), (7, 7), (1, 6), (3, 7), (2, 5), (7, 2),
#                (1, 2), (6, 7), (5, 5), (3, 3), (7, 6), (6, 3), (2, 2), (4, 1),
#                (1, 1), (6, 4), (4, 5), (7, 5), (4, 2), (6, 5), (3, 5), (2, 7),
#                (4, 6), (6, 1), (3, 1), (5, 7), (7, 4), (4, 3)]

# if no inputs given run default
if len(sys.argv) <= 1:
    print("Using default test cases:")
    test_inputs = [(4, 6), (4, 5), (5, 5), (4, 0), (5, 0), (4, 1), (4, 2), (4, 3),
                   (4, 4)]
else:

    try:
        for i, arg in enumerate(sys.argv[1:]):
            inputs = arg.split(",")
            test_inputs.append((int(inputs[0]), int(inputs[1])))
    except:
        print("Check your inputs and try again")
        exit(1)


print(
    "{:<9} {:<4} {:<4} {:<10} {:<15}".format("Searcher", "N", "K", "expansions",
                                             "Result"))
for i in test_inputs:
    bfs = breadth_first_tree_search(NQueensDefectedProblem(i[0], i[1]))
    dfs = depth_first_tree_search(NQueensDefectedProblem(i[0], i[1]))
    dls = depth_limited_search(NQueensDefectedProblem(i[0], i[1]))
    ids = iterative_deepening_search(NQueensDefectedProblem(i[0], i[1]))

    print("{:<9} {:<4} {:<4} {:<10} {:<15}".format("BFS", str(i[0]), str(i[1]),
                                                   str(bfs[1]), str(bfs[0])))

    print("{:<9} {:<4} {:<4} {:<10} {:<15}".format("DFS", str(i[0]), str(i[1]),
                                                   str(dfs[1]), str(dfs[0])))

    print("{:<9} {:<4} {:<4} {:<10} {:<15}".format("DLS", str(i[0]), str(i[1]),
                                                   str(dls[1]), str(dls[0])))

    print("{:<9} {:<4} {:<4} {:<10} {:<15}".format("IDS", str(i[0]), str(i[1]),
                                                   str(ids[1]), str(ids[0])))
    print()
