import math
import random

class MCTSNode:
    def __init__(self, state, parent=None):
        self.state = state
        self.parent = parent
        self.children = []
        self.visits = 0
        self.value = 0

    def is_fully_expanded(self):
        return len(self.children) == len(self.state.get_legal_actions())

    def best_child(self, c_param=1.4):
        choices_weights = [
            (child.value / child.visits) + c_param * math.sqrt((2 * math.log(self.visits) / child.visits))
            for child in self.children
        ]
        return self.children[choices_weights.index(max(choices_weights))]

    def expand(self):
        action = random.choice(self.state.get_legal_actions())
        next_state = self.state.move(action)
        child_node = MCTSNode(next_state, parent=self)
        self.children.append(child_node)
        return child_node

    def update(self, reward):
        self.visits += 1
        self.value += reward

def mcts(root, iterations):
    for _ in range(iterations):
        node = root
        while node.is_fully_expanded():
            node = node.best_child()
        if not node.state.is_terminal():
            node = node.expand()
        reward = node.state.simulate()
        while node is not None:
            node.update(reward)
            node = node.parent
    return root.best_child(c_param=0)

class GameState:
    def __init__(self, task_list):
        self.task_list = task_list
        self.current_task_index = 0
        self.task_status = {task: "pending" for task in task_list}

    def get_legal_actions(self):
        # Generalize to handle a dynamic range of task dependencies
        actions = []
        for i in range(self.current_task_index, len(self.task_list)):
            if self.task_list[i] == "task1" and "task2" not in self.task_list[:i]:
                actions.append(self.task_list[i])
            elif self.task_list[i] == "task2" and "task1" in self.task_list[:i]:
                actions.append(self.task_list[i])
            else:
                actions.append(self.task_list[i])
        return actions

    def move(self, action):
        # Reflect state transitions for actions with multiple effects or outcomes
        new_state = GameState(self.task_list)
        new_state.current_task_index = self.current_task_index + 1
        new_state.task_status = self.task_status.copy()
        new_state.task_status[action] = "completed"
        return new_state

    def is_terminal(self):
        # Account for more complex conditions that define a terminal state
        return self.current_task_index >= len(self.task_list)

    def simulate(self):
        # Incorporate more detailed criteria for simulation
        task = self.task_list[self.current_task_index]
        if task == "task1":
            return random.uniform(0.7, 0.9)  # Higher reward for task1 with some variability
        elif task == "task2":
            return random.uniform(0.2, 0.4)  # Lower reward for task2 with some variability
        else:
            return random.uniform(0.4, 0.6)  # Default reward for other tasks with some variability

# Example usage:
# initial_state = GameState(["task1", "task2", "task3"])
# root = MCTSNode(initial_state)
# best_action = mcts(root, 1000).state
