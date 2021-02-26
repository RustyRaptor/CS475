from search import *
from utils import *


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
        if problem.goal_test(node.state):
            return node, expansions
        frontier.extend(node.expand(problem))
        expansions += 1
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
        if problem.goal_test(node.state):
            return node, expansions
        frontier.extend(node.expand(problem))
        expansions += 1
    return None, expansions


def conflict(row1, col1, row2, col2):
    """Would putting two queens in (row1, col1) and (row2, col2) conflict?"""
    return (row1 == row2 or  # same row
            col1 == col2 or  # same column
            row1 - col1 == row2 - col2 or  # same \ diagonal
            row1 + col1 == row2 + col2)  # same / diagonal


class NQueensDefectedProblem(Problem):
    """
    Ziad:

    This is a modified version of NQueensProblem from search.py which changes the 
    goal_test() to make use of the h() function and count how many
    conflicting queens there are.
    """

    def __init__(self, N, K):
        super().__init__(tuple([-1] * N))
        self.N = N
        self.K = K

    def actions(self, state):
        """In the leftmost empty column, try all non-conflicting rows."""
        if state[-1] != -1:
            return []  # All columns filled; no successors
        else:
            col = state.index(-1)
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

    def conflicted(self, state, row, col):
        """Would placing a queen at (row, col) conflict with anything?"""
        return any(conflict(row, col, state[c], c)
                   for c in range(col))

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

        return (self.number_of_conflicting_pairs(state)) == self.K

    def h(self, node):
        """Return number of conflicting queens for a given node"""
        num_conflicts = 0
        for (r1, c1) in enumerate(node.state):
            for (r2, c2) in enumerate(node.state):
                if (r1, c1) != (r2, c2):
                    num_conflicts += conflict(r1, c1, r2, c2)

        return num_conflicts

    def number_of_conflicting_pairs(self, state):
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


a = [(5, 5), (4, 6), (4, 5), (4, 2), (4, 7)]

# print("N=5, K=5", depth_first_tree_search(NQueensDefectedProblem(5, 5)))
# print("N=4, K=6", depth_first_tree_search(NQueensDefectedProblem(4, 6)))
# print("N=4, K=5", depth_first_tree_search(NQueensDefectedProblem(4, 5)))
# print("N=4, K=2", depth_first_tree_search(NQueensDefectedProblem(4, 2)))
# print("N=4, K=7", depth_first_tree_search(NQueensDefectedProblem(4, 7)))

print("Searcher\tInputs\tResults")
for i in a:
    print("BFS\tN=", i[0], "K=", i[1], "\t", breadth_first_tree_search(NQueensDefectedProblem(i[0], i[1])))
    print("DFS\tN=", i[0], "K=", i[1], "\t", depth_first_tree_search(NQueensDefectedProblem(i[0], i[1])))
    print("DLS\tN=", i[0], "K=", i[1], "\t", depth_limited_search(NQueensDefectedProblem(i[0], i[1])))
    print("IDS\tN=", i[0], "K=", i[1], "\t", iterative_deepening_search(NQueensDefectedProblem(i[0], i[1])))
