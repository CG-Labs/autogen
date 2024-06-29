import unittest
import random
from mcts_implementation import MCTSNode, GameState, mcts

class TestMCTSImplementation(unittest.TestCase):

    def setUp(self):
        self.task_list = ["task1", "task2", "task3"]
        self.initial_state = GameState(self.task_list)
        self.root = MCTSNode(self.initial_state)

    def test_get_legal_actions(self):
        actions = self.initial_state.get_legal_actions()
        self.assertEqual(actions, ["task1", "task2", "task3"])

    def test_move(self):
        new_state = self.initial_state.move("task1")
        self.assertEqual(new_state.current_task_index, 1)
        self.assertEqual(new_state.task_status["task1"], "completed")

    def test_is_terminal(self):
        terminal_state = GameState(self.task_list)
        terminal_state.current_task_index = len(self.task_list)
        self.assertTrue(terminal_state.is_terminal())

    def test_simulate(self):
        reward = self.initial_state.simulate()
        self.assertTrue(0.0 <= reward <= 0.9)

    def test_mcts(self):
        best_action_node = mcts(self.root, 1000)
        if best_action_node is not None:
            self.assertIn(best_action_node.state.task_list[best_action_node.state.current_task_index], self.task_list)
        else:
            self.assertIsNone(best_action_node)

    def test_best_child_no_children(self):
        empty_node = MCTSNode(self.initial_state)
        empty_node.children = []
        best_child = empty_node.best_child()
        self.assertIsNone(best_child)

    def test_mcts_no_children(self):
        root_with_no_children = MCTSNode(self.initial_state)
        root_with_no_children.children = []
        best_action_node = mcts(root_with_no_children, 1000)
        print(f"Debug: root_with_no_children.children = {root_with_no_children.children}")
        print(f"Debug: best_action_node = {best_action_node}")
        self.assertIsNotNone(best_action_node)
        self.assertIn(best_action_node.state.task_list[best_action_node.state.current_task_index], self.task_list)

if __name__ == '__main__':
    unittest.main()
