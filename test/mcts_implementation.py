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

    def get_legal_actions(self):
        # Return a list of possible actions (e.g., next task to perform)
        if self.current_task_index < len(self.task_list):
            # Example of more complex decision-making process
            actions = []
            for i in range(self.current_task_index, len(self.task_list)):
                if self.task_list[i] == "task1" and "task2" not in self.task_list[:i]:
                    actions.append(self.task_list[i])
                elif self.task_list[i] == "task2" and "task1" in self.task_list[:i]:
                    actions.append(self.task_list[i])
                else:
                    actions.append(self.task_list[i])
            return actions
        return []

    def move(self, action):
        # Move to the next task in the list
        new_state = GameState(self.task_list)
        new_state.current_task_index = self.current_task_index + 1
        return new_state

    def is_terminal(self):
        # Determine if all tasks have been completed
        return self.current_task_index >= len(self.task_list)

    def simulate(self):
        # Simulate the outcome of performing the current task
        # For simplicity, return a random reward
        task = self.task_list[self.current_task_index]
        # Simulate task outcome based on task type or other criteria
        if task == "task1":
            return random.uniform(0.5, 1)  # Higher reward for task1
        elif task == "task2":
            return random.uniform(0, 0.5)  # Lower reward for task2
        else:
            return random.uniform(0, 1)  # Default random reward

# Example usage:
# initial_state = GameState(["task1", "task2", "task3"])
# root = MCTSNode(initial_state)
# best_action = mcts(root, 1000).state
