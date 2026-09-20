class Graph:
	"""Draw a simple auto-sized X/Y line graph."""

	def insert_graph(self, graph, x_values, y_values):
		if not x_values or not y_values:
			raise ValueError("Graph data cannot be empty")
		if len(x_values) != len(y_values):
			raise ValueError("X and Y data must have the same length")

		graph.erase()
		points = list(zip(x_values, y_values))
		y_min, y_max = min(y_values), max(y_values)

		graph_left = 20
		graph_right = 90
		x_axis_left = graph_left - 5
		x_axis_right = graph_right + 5
		step = (graph_right - graph_left) / max(1, len(points) - 1)
		x_axis = 50 if y_min <= 0 <= y_max else 10
		plot_bottom = x_axis + 5
		plot_top = 90

		def scale_y(value):
			if y_min == y_max:
				return plot_bottom
			return plot_bottom + ((value - y_min) * (plot_top - plot_bottom)
								 / (y_max - y_min))

		scaled_points = [
			(graph_left + index * step, scale_y(y))
			for index, (_, y) in enumerate(points)
		]
		graph.draw_line((x_axis_left, x_axis), (x_axis_right, x_axis),
						color="black", width=2)
		graph.draw_text("X", (92, x_axis), color="black")

		for index, x_value in enumerate(x_values):
			x_position = graph_left + index * step
			graph.draw_text(
				str(x_value), (x_position, max(2, x_axis - 4)), color="black")

		for start, end in zip(scaled_points, scaled_points[1:]):
			graph.draw_line(start, end, color="black", width=2)
		for point, (x_value, y_value) in zip(scaled_points, points):
			graph.draw_circle(point, 1.5, fill_color="black", line_color="black")
			graph.draw_text(
				f"({x_value}, {y_value})",
				(point[0] + 2, point[1] + 5),
				color="red",
			)

	def draw(self, graph, x_values, y_values):
		"""Keep the old method name available for compatibility."""
		self.insert_graph(graph, x_values, y_values)
