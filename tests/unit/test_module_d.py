# path handler
import sys
import os

PROJECT_ROOT = os.path.abspath(os.path.join(
    os.path.dirname(__file__), "..", ".."))
SRC_DIR = os.path.join(PROJECT_ROOT, "src")

for module_path in (PROJECT_ROOT, SRC_DIR):
    if os.path.isdir(module_path) and module_path not in sys.path:
        sys.path.insert(0, module_path)

# start of the unit test code
import unittest
from src.module_d.graph import Graph


class FakeGraph:
    def __init__(self):
        self.lines = []
        self.points = []
        self.text = []

    def erase(self):
        pass

    def draw_line(self, start, end, **kwargs):
        self.lines.append((start, end, kwargs))

    def draw_circle(self, point, *args, **kwargs):
        self.points.append(point)

    def draw_text(self, text, location, **kwargs):
        self.text.append((text, location, kwargs))


class TestGraph(unittest.TestCase):
    def setUp(self):
        self.graph = Graph()
        self.canvas = FakeGraph()

    def test_insert_graph_draws_points_and_lines(self):
        self.graph.insert_graph(self.canvas, [1, 2, 3], [10, 20, 30])

        self.assertEqual(len(self.canvas.points), 3)
        self.assertEqual(len(self.canvas.lines), 3)

    def test_x_points_are_evenly_spaced(self):
        self.graph.insert_graph(self.canvas, [2, 3, 4], [10, 20, 30])

        x_positions = [point[0] for point in self.canvas.points]
        self.assertEqual(x_positions, [20, 55, 90])

    def test_lowest_y_value_is_five_pixels_above_x_axis(self):
        self.graph.insert_graph(self.canvas, [1, 2], [20, 10])

        x_axis_y = self.canvas.lines[0][0][1]
        self.assertEqual(self.canvas.points[1][1], x_axis_y + 5)
        self.assertGreater(self.canvas.points[0][1], self.canvas.points[1][1])

    def test_equal_y_values_are_drawn_on_one_horizontal_line(self):
        self.graph.insert_graph(self.canvas, [1, 2, 3], [10, 10, 10])

        y_positions = [point[1] for point in self.canvas.points]
        self.assertEqual(y_positions, [y_positions[0]] * 3)
        x_axis_y = self.canvas.lines[0][0][1]
        self.assertEqual(y_positions, [x_axis_y + 5] * 3)

    def test_points_keep_x_y_pairs_when_drawing_lines(self):
        self.graph.insert_graph(self.canvas, [10, 20, 30], [30, 10, 20])

        labels = [text for text, _, _ in self.canvas.text]
        self.assertIn("(10, 30)", labels)
        self.assertIn("(20, 10)", labels)
        self.assertIn("(30, 20)", labels)

    def test_graph_contains_axis_and_point_labels(self):
        self.graph.insert_graph(self.canvas, [1, 2], [10, 20])

        labels = [text for text, _, _ in self.canvas.text]
        self.assertIn("X", labels)
        self.assertIn("1", labels)
        self.assertIn("(1, 10)", labels)
        self.assertNotIn("10", labels)
        self.assertNotIn("20", labels)

    def test_empty_data_raises_error(self):
        with self.assertRaises(ValueError):
            self.graph.insert_graph(self.canvas, [], [])

    def test_different_data_lengths_raise_error(self):
        with self.assertRaises(ValueError):
            self.graph.insert_graph(self.canvas, [1, 2], [10])


if __name__ == "__main__":
    unittest.main()