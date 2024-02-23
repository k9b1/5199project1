"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""
import util
class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).
    You do not need to change anything in this class, ever.
    """
    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()
    def isGoalState(self, state):
        """
          state: Search state
        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()
    def getSuccessors(self, state):
        """
          state: Search state
        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()
    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take
        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()
def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem: SearchProblem):
    """
    Search the deepest nodes in the search tree first.
    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.
    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:
    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()
    currentState = (problem.getStartState(), []);
    fringe = util.Stack()
    seen = set()
    seen.add(currentState[0]);
    while not problem.isGoalState(currentState[0]):
        successorStates = problem.getSuccessors(currentState[0]);
        for state in successorStates:
            if not state[0] in seen:
                fringe.push((state[0], [*currentState[1], state[1]]))
        if fringe.isEmpty():
            raise ValueError('Fringe is empty but did not find a solution')
        currentState = fringe.pop()
        seen.add(currentState[0])
    return currentState[1];

def breadthFirstSearch(problem: SearchProblem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()
    currentState = (problem.getStartState(), []);
    fringe = util.Queue()
    seen = set()
    seen.add(currentState[0]);
    while not problem.isGoalState(currentState[0]):
        successorStates = problem.getSuccessors(currentState[0]);
        for state in successorStates:
            if not state[0] in seen:
                seen.add(state[0])
                fringe.push((state[0], [*currentState[1], state[1]]))
        if fringe.isEmpty():
            raise ValueError('Fringe is empty but did not find a solution')
        currentState = fringe.pop()
    return currentState[1];

def depthFirstSearch(problem):
    from util import Stack

    stack = Stack()
    visited = set()
    stack.push((problem.getStartState(), [], 0))

    while not stack.isEmpty():
        currentState, actions, currentCost = stack.pop()

        if problem.isGoalState(currentState):
            return actions

        if currentState not in visited:
            visited.add(currentState)
            for nextState, action, cost in problem.getSuccessors(currentState):
                if nextState not in visited:
                    newActions = actions + [action]
                    stack.push((nextState, newActions, currentCost + cost))

    return [];

def uniformCostSearch(problem: SearchProblem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()
    currentState = (problem.getStartState(), [], 0)
    fringe = util.PriorityQueue()
    seen = { currentState[0]: 0 }
    while not problem.isGoalState(currentState[0]):
        successorStates = problem.getSuccessors(currentState[0])
        for state in successorStates:
            # make sure cost is the total cost of travel, not just the next step
            totalCost = state[2] + currentState[2]
            # double check if the already seen node has a cheap path to it
            if not state[0] in seen or totalCost < seen[state[0]]:
                seen[state[0]] = totalCost
                fringe.push((state[0], [*currentState[1], state[1]], totalCost), totalCost)
        if fringe.isEmpty():
            raise ValueError('Fringe is empty but did not find a solution')
        currentState = fringe.pop()
    return currentState[1];

def breadthFirstSearch(problem: SearchProblem):
    from util import Queue

    queue = Queue()
    visited = set()
    queue.push((problem.getStartState(), []))

    while not queue.isEmpty():
        currentState, path = queue.pop()

        if problem.isGoalState(currentState):
            return path

        if currentState not in visited:
            visited.add(currentState)
            for nextState, action, cost in problem.getSuccessors(currentState):
                if nextState not in visited:
                    queue.push((nextState, path + [action]))

    return [];

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0
def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()
# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch

def uniformCostSearch(problem: SearchProblem):
    from util import PriorityQueue

    fringe = PriorityQueue()
    visited = set()
    startState = problem.getStartState()
    fringe.push((startState, [], 0), 0)  # state, actions, cost

    while not fringe.isEmpty():
        currentState, actions, currentCost = fringe.pop()

        if problem.isGoalState(currentState):
            return actions

        if currentState not in visited:
            visited.add(currentState)
            for nextState, action, cost in problem.getSuccessors(currentState):
                if nextState not in visited:
                    newActions = actions + [action]
                    newCost = currentCost + cost
                    fringe.push((nextState, newActions, newCost), newCost)

    return [];
