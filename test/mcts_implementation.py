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
    def get_legal_actions(self):
        # Placeholder implementation: Return a list of dummy actions
        return ["action1", "action2", "action3"]

    def move(self, action):
        # Placeholder implementation: Return a new GameState instance
        return GameState()

    def is_terminal(self):
        # Placeholder implementation: Randomly determine if the state is terminal
        return random.choice([True, False])

    def simulate(self):
        # Placeholder implementation: Return a random reward
        return random.uniform(0, 1)

# Example usage:
# root = MCTSNode(initial_state)
# best_action = mcts(root, 1000).state
