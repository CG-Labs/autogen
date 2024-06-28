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
        legal_actions = self.state.get_legal_actions()
        return len(self.children) == len(legal_actions) and all(child.state in [self.state.move(action) for action in legal_actions] for child in self.children)

    def best_child(self, c_param=1.4):
        if not self.children:
            return None
        choices_weights = [
            (child.value / child.visits) + c_param * math.sqrt((2 * math.log(self.visits) / child.visits))
            for child in self.children if child.visits > 0
        ]
        return self.children[choices_weights.index(max(choices_weights))] if choices_weights else None

    def expand(self):
        legal_actions = self.state.get_legal_actions()
        if not legal_actions:
            return None
        for action in legal_actions:
            next_state = self.state.move(action)
            if next_state not in [child.state for child in self.children]:
                child_node = MCTSNode(next_state, parent=self)
                self.children.append(child_node)
                return child_node
        return None

    def update(self, reward):
        self.visits += 1
        self.value += reward

def mcts(root, iterations, c_param=1.4):
    legal_actions = root.state.get_legal_actions()
    if not legal_actions:
        return None
    for _ in range(iterations):
        node = root
        while node.is_fully_expanded():
            node = node.best_child(c_param)
            if node is None:
                break
        if node is not None and not node.state.is_terminal():
            node = node.expand()
        if node is None:
            break
        reward = node.state.simulate() if node is not None else 0.0
        while node is not None:
            node.update(reward)
            node = node.parent
    best_child = root.best_child(c_param=0)
    return best_child if best_child is not None else None

class GameState:
    def __init__(self, task_list):
        self.task_list = task_list
        self.current_task_index = 0
        self.task_status = {task: "pending" for task in task_list}

    def get_legal_actions(self):
        actions = []
        for i in range(self.current_task_index, len(self.task_list)):
            task = self.task_list[i]
            if self._can_execute_task(task):
                actions.append(task)
        return actions

    def _can_execute_task(self, task):
        # Generalized logic for task dependencies
        if task in self.task_status and self.task_status[task] == "pending":
            return True
        return False

    def move(self, action):
        new_state = GameState(self.task_list)
        new_state.current_task_index = self.current_task_index + 1
        new_state.task_status = self.task_status.copy()
        new_state.task_status[action] = "completed"
        return new_state

    def is_terminal(self):
        return self.current_task_index >= len(self.task_list)

    def simulate(self):
        if self.current_task_index < len(self.task_list):
            task = self.task_list[self.current_task_index]
            # Refined logic for task rewards based on complexity, priority, and estimated time
            task_complexity = {"task1": 0.9, "task2": 0.4, "task3": 0.6}
            task_priority = {"task1": 0.8, "task2": 0.3, "task3": 0.5}
            task_time = {"task1": 0.7, "task2": 0.2, "task3": 0.4}
            complexity_reward = task_complexity.get(task, 0.5)
            priority_reward = task_priority.get(task, 0.5)
            time_reward = task_time.get(task, 0.5)
            return random.uniform(0.4, 0.6) * complexity_reward * priority_reward * time_reward
        else:
            return 0.0

# Example usage:
# initial_state = GameState(["task1", "task2", "task3"])
# root = MCTSNode(initial_state)
# best_action = mcts(root, 1000).state
