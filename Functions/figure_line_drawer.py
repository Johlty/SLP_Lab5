

def draw(self, colored=True):
        """Малюємо паралелепіпед на основі його проєктованих вершин"""
        # Проектуємо всі вершини в 2D
        projected_vertices = [self.project_vertex(v) for v in self.vertices]
        
        # Знаходимо мінімальні та максимальні координати для визначення розміру полотна
        min_x = min(v[0] for v in projected_vertices)
        max_x = max(v[0] for v in projected_vertices)
        min_y = min(v[1] for v in projected_vertices)
        max_y = max(v[1] for v in projected_vertices)
        
        canvas_width = max_x - min_x + 1
        canvas_height = max_y - min_y + 1

        # Створюємо сітку для малювання, динамічний розмір
        grid = [[' ' for _ in range(canvas_width)] for _ in range(canvas_height)]

        # Відображаємо лінії між відповідними вершинами паралелепіпеда
        edges = [
            (0, 1), (1, 2), (2, 3), (3, 0),  # Задня грань
            (4, 5), (5, 6), (6, 7), (7, 4),  # Передня грань
            (0, 4), (1, 5), (2, 6), (3, 7)   # З'єднання передньої і задньої граней
        ]
        
        for edge in edges:
            v1 = projected_vertices[edge[0]]
            v2 = projected_vertices[edge[1]]
            self.draw_line(grid, v1, v2, min_x, min_y, colored)

        return grid  # Повертаємо сітку для подальшого виведення або збереження

def draw_line(self, grid, start, end, min_x, min_y, colored):
        """Малюємо лінію між двома точками (Брезенхемовий алгоритм)"""
        x1, y1 = start
        x2, y2 = end
        dx = abs(x2 - x1)
        dy = abs(y2 - y1)
        sx = 1 if x1 < x2 else -1
        sy = 1 if y1 < y2 else -1
        err = dx - dy

        while True:
            if 0 <= x1 - min_x < len(grid[0]) and 0 <= y1 - min_y < len(grid):
                if colored:
                    grid[y1 - min_y][x1 - min_x] = self.console_color  # Кольоровий символ
                else:
                    grid[y1 - min_y][x1 - min_x] = self.color  # Безкольоровий символ
            if x1 == x2 and y1 == y2:
                break
            e2 = err * 2
            if e2 > -dy:
                err -= dy
                x1 += sx
            if e2 < dx:
                err += dx
                y1 += sy