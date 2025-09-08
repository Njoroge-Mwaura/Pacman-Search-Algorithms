# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util
from game import Directions
from typing import List
from typing import Any, Set, Tuple


# Lightweight search logging (optional)
def _log_search_event(message: str) -> None:
    try:
        with open("search_log.txt", "a") as f:
            f.write(message + "\n")
    except Exception:
        pass


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


def tinyMazeSearch(problem: SearchProblem) -> List[Directions]:
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem: SearchProblem) -> List[Directions]:
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
    stack = util.Stack()
    start_state = problem.getStartState()
    stack.push((start_state, []))
    visited: Set[Any] = set()

    _log_search_event(f"DFS start: {start_state}")

    while not stack.isEmpty():
        state, path = stack.pop()
        if state in visited:
            continue
        visited.add(state)
        _log_search_event(f"DFS expand: {state} | path_len={len(path)}")

        if problem.isGoalState(state):
            _log_search_event(f"DFS goal: {state} | path_len={len(path)}")
            return path

        for successor, action, _ in problem.getSuccessors(state):
            if successor not in visited:
                stack.push((successor, path + [action]))

    return []


def breadthFirstSearch(problem: SearchProblem) -> List[Directions]:
    """Search the shallowest nodes in the search tree first."""
    queue = util.Queue()
    start_state = problem.getStartState()
    queue.push((start_state, []))
    visited: Set[Any] = set([start_state])

    _log_search_event(f"BFS start: {start_state}")

    while not queue.isEmpty():
        state, path = queue.pop()
        _log_search_event(f"BFS expand: {state} | path_len={len(path)}")
        if problem.isGoalState(state):
            _log_search_event(f"BFS goal: {state} | path_len={len(path)}")
            return path
        for successor, action, _ in problem.getSuccessors(state):
            if successor not in visited:
                visited.add(successor)
                queue.push((successor, path + [action]))

    return []


def uniformCostSearch(problem: SearchProblem) -> List[Directions]:
    """Search the node of least total cost first."""

    def priority_fn(item: Tuple[Any, List[Directions], float]) -> float:
        _, __, cost = item
        return cost

    frontier = util.PriorityQueueWithFunction(priority_fn)
    start_state = problem.getStartState()
    frontier.push((start_state, [], 0.0))
    best_g: dict[Any, float] = {start_state: 0.0}

    _log_search_event(f"UCS start: {start_state}")

    while not frontier.isEmpty():
        state, path, g = frontier.pop()
        _log_search_event(f"UCS expand: {state} | g={g} | path_len={len(path)}")
        if problem.isGoalState(state):
            _log_search_event(f"UCS goal: {state} | g={g} | path_len={len(path)}")
            return path
        for successor, action, step_cost in problem.getSuccessors(state):
            new_g = g + step_cost
            if successor not in best_g or new_g < best_g[successor]:
                best_g[successor] = new_g
                frontier.push((successor, path + [action], new_g))

    return []


def nullHeuristic(state, problem=None) -> float:
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic) -> List[Directions]:
    """Search the node that has the lowest combined cost and heuristic first."""

    def priority_fn(item: Tuple[Any, List[Directions], float]) -> float:
        state, __, g_cost = item
        return g_cost + float(heuristic(state, problem))

    frontier = util.PriorityQueueWithFunction(priority_fn)
    start_state = problem.getStartState()
    frontier.push((start_state, [], 0.0))
    best_g: dict[Any, float] = {start_state: 0.0}

    _log_search_event(f"A* start: {start_state}")

    while not frontier.isEmpty():
        state, path, g_cost = frontier.pop()
        _log_search_event(
            f"A* expand: {state} | g={g_cost} h={heuristic(state, problem)} | path_len={len(path)}"
        )
        if problem.isGoalState(state):
            _log_search_event(f"A* goal: {state} | g={g_cost} | path_len={len(path)}")
            return path
        for successor, action, step_cost in problem.getSuccessors(state):
            new_g = g_cost + step_cost
            if successor not in best_g or new_g < best_g[successor]:
                best_g[successor] = new_g
                frontier.push((successor, path + [action], new_g))

    return []


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
