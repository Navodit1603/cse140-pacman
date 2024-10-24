"""
In this file, you will implement generic search algorithms which are called by Pacman agents.
"""

from pacai.util.stack import Stack
from pacai.util.queue import Queue
from pacai.util.priorityQueue import PriorityQueue
from pacai.core.search.heuristic import manhattan

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first [p 85].

    Your search algorithm needs to return a list of actions that reaches the goal.
    Make sure to implement a graph search algorithm [Fig. 3.7].

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:
    ```
    print("Start: %s" % (str(problem.startingState())))
    print("Is the start a goal?: %s" % (problem.isGoal(problem.startingState())))
    print("Start's successors: %s" % (problem.successorStates(problem.startingState())))
    ```
    """

    # *** Your Code Here ***
    
    s = Stack()
    s.push(problem.startingState()) 
    visited = set() 
    parents = {problem.startingState(): None}

    print("Start: %s" % str(problem.startingState()))
    print("Is the start a goal?: %s" % problem.isGoal(problem.startingState()))

    
    if problem.isGoal(problem.startingState()):
        return []

    
    while not s.isEmpty():
        node = s.pop() 

        
        if problem.isGoal(node):
            print("Goal found!")
            
            path = []
            while node != problem.startingState():
                parent, action = parents[node]
                path.insert(0, action)
                node = parent
            return path

        if node not in visited:
            visited.add(node) 
            print(f"Visiting node: {node}")
            successors = problem.successorStates(node)
            print(f"Successors of {node}: {successors}")

            for successor, action, _ in successors:
                if successor not in visited:
                    s.push(successor)
                    parents[successor] = (node,action)

    return "Failure" 


def breadthFirstSearch(problem):
    """
    Search the shallowest nodes in the search tree first. [p 81]
    """

    # *** Your Code Here ***
    s = Queue()
    s.push(problem.startingState()) 
    visited = set() 
    parents = {problem.startingState(): None}

    print("Start: %s" % str(problem.startingState()))
    print("Is the start a goal?: %s" % problem.isGoal(problem.startingState()))

    
    if problem.isGoal(problem.startingState()):
        return []

    
    while not s.isEmpty():
        node = s.pop() 

        
        if problem.isGoal(node):
            print("Goal found!")
            
            path = []
            while node != problem.startingState():
                parent, action = parents[node]
                path.insert(0, action)
                node = parent
            return path

        if node not in visited:
            visited.add(node) 
            print(f"Visiting node: {node}")
            successors = problem.successorStates(node)
            print(f"Successors of {node}: {successors}")

            for successor, action, _ in successors:
                if successor not in visited:
                    s.push(successor)
                    parents[successor] = (node,action)

    return "Failure" 

def uniformCostSearch(problem):
    """
    Search the node of least total cost first.
    """

    # *** Your Code Here ***
    s = PriorityQueue()
    s.push(problem.startingState(), 0) 
    visited = set() 
    parents = {problem.startingState(): None}
    path_cost = {problem.startingState(): 0}

    print("Start: %s" % str(problem.startingState()))
    print("Is the start a goal?: %s" % problem.isGoal(problem.startingState()))

    
    if problem.isGoal(problem.startingState()):
        return []

    
    while not s.isEmpty():
        node = s.pop() 

        
        if problem.isGoal(node):
            print("Goal found!")
            
            path = []
            while node != problem.startingState():
                parent, action = parents[node]
                path.insert(0, action)
                node = parent
            return path

        if node not in visited:
            visited.add(node) 
            print(f"Visiting node: {node}")
            successors = problem.successorStates(node)
            print(f"Successors of {node}: {successors}")

            for successor, action, cost in successors:
                new_cost = path_cost[node] + cost
                if successor not in visited or new_cost < path_cost.get(successor, float('inf')):
                    s.push(successor, new_cost)
                    path_cost[successor] = new_cost
                    parents[successor] = (node,action)

    return "Failure" 
    

def aStarSearch(problem, heuristic):
    """
    Search the node that has the lowest combined cost and heuristic first.
    """

    # *** Your Code Here ***
    s = PriorityQueue()
    s.push(problem.startingState(), 0) 
    visited = set() 
    parents = {problem.startingState(): None}
    path_cost = {problem.startingState(): 0}

    print("Start: %s" % str(problem.startingState()))
    print("Is the start a goal?: %s" % problem.isGoal(problem.startingState()))

    
    if problem.isGoal(problem.startingState()):
        return []

    
    while not s.isEmpty():
        node = s.pop() 

        
        if problem.isGoal(node):
            print("Goal found!")
            
            path = []
            while node != problem.startingState():
                parent, action = parents[node]
                path.insert(0, action)
                node = parent
            return path

        if node not in visited:
            visited.add(node) 
            print(f"Visiting node: {node}")
            successors = problem.successorStates(node)
            print(f"Successors of {node}: {successors}")

            for successor, action, cost in successors:
                new_cost = path_cost[node] + cost
                heuristic_cost = manhattan(successor, problem)
                weight = new_cost + heuristic_cost
                if successor not in visited or new_cost < path_cost.get(successor, float('inf')):                    
                    s.push(successor, weight)
                    path_cost[successor] = new_cost
                    parents[successor] = (node,action)

    return "Failure" 
