import math 

class Parallelepiped3D:
    def __init__(self, length, width, height, color, console_color):
        self.length = length
        self.width = width
        self.height = height
        self.color = color  # Символ без кольору для файлу
        self.console_color = console_color  # Кольоровий символ для консолі
        self.vertices = self.create_vertices()

    def create_vertices(self):
        """Створюємо 8 вершин паралелепіпеда"""
        l = self.length / 4
        w = self.width / 4
        h = self.height / 4
        return [
            [-l, -w, -h], [l, -w, -h], [l, w, -h], [-l, w, -h],  # Задня грань
            [-l, -w, h], [l, -w, h], [l, w, h], [-l, w, h]       # Передня грань
        ]

    def rotate_y(self, angle):
        """Обертання паралелепіпеда навколо осі Y (в градусах)"""
        angle = math.radians(angle)  # Конвертуємо в радіани
        cos_angle = math.cos(angle)
        sin_angle = math.sin(angle)
        for vertex in self.vertices:
            x = vertex[0]
            z = vertex[2]
            vertex[0] = x * cos_angle - z * sin_angle
            vertex[2] = x * sin_angle + z * cos_angle

    def rotate_x(self, angle):
        """Обертання паралелепіпеда навколо осі X (в градусах)"""
        angle = math.radians(angle)  # Конвертуємо в радіани
        cos_angle = math.cos(angle)
        sin_angle = math.sin(angle)
        for vertex in self.vertices:
            y = vertex[1]
            z = vertex[2]
            vertex[1] = y * cos_angle - z * sin_angle
            vertex[2] = y * sin_angle + z * cos_angle

    def rotate_z(self, angle):
        """Обертання паралелепіпеда навколо осі Z (в градусах)"""
        angle = math.radians(angle)  # Конвертуємо в радіани
        cos_angle = math.cos(angle)
        sin_angle = math.sin(angle)
        for vertex in self.vertices:
            x = vertex[0]
            y = vertex[1]
            vertex[0] = x * cos_angle - y * sin_angle
            vertex[1] = x * sin_angle + y * cos_angle

    def project_vertex(self, vertex):
        """Проектуємо вершину 3D у 2D"""
        distance = 5  # Відстань до спостерігача
        factor = distance / (distance + vertex[2])
        
        # Масштабування не прив'язане до фіксованого полотна
        x_proj = int(vertex[0] * factor * 10)
        y_proj = int(vertex[1] * factor * 10)
        return (x_proj, y_proj)

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

    def save_to_file(self, filename, grid):
        """Зберігає ASCII-арт у текстовий файл"""
        with open(filename, 'w') as file:
            for row in grid:
                file.write(''.join(row) + '\n')


































def main():
    while True:
        try:
            length = float(input("Введіть довжину паралелепіпеда (макс 10): "))
            if not (0 < length <= 10):
                raise ValueError("Довжина має бути від 0 до 10.")
            width = float(input("Введіть ширину паралелепіпеда (макс 10): "))
            if not (0 < width <= 10):
                raise ValueError("Ширина має бути від 0 до 10.")
            height = float(input("Введіть висоту паралелепіпеда (макс 10): "))
            if not (0 < height <= 10):
                raise ValueError("Висота має бути від 0 до 10.")
            break
        except ValueError as e:
            print(f"Помилка: {e}. Будь ласка, введіть число в межах 0-10.")
    
    while True:
        print("Виберіть колір для паралелепіпеда:")
        print("1 - Червоний")
        print("2 - Зелений")
        print("3 - Синій")
        print("4 - Жовтий")
        print("5 - Фіолетовий")
        color_choice = input("Ваш вибір (1-5): ")
        color_map = {
            '1': ('#', '\033[91m#\033[0m'),  # Червоний
            '2': ('#', '\033[92m#\033[0m'),  # Зелений
            '3': ('#', '\033[94m#\033[0m'),  # Синій
            '4': ('#', '\033[93m#\033[0m'),  # Жовтий
            '5': ('#', '\033[95m#\033[0m')   # Фіолетовий
        }
        if color_choice in color_map:
            color, console_color = color_map[color_choice]
            break
        else:
            print("Невірний вибір. Будь ласка, виберіть число від 1 до 5.")

    parallelepiped = Parallelepiped3D(length, width, height, color, console_color)

    while True:
        axis = input("Виберіть вісь обертання (x/y/z): ").lower()
        try:
            angle = float(input("Введіть кут обертання (в градусах, наприклад 45): "))
        except ValueError:
            print("Невірне значення кута. Введіть число.")
            continue
        
        if axis == 'x':
            parallelepiped.rotate_x(angle)
        elif axis == 'y':
            parallelepiped.rotate_y(angle)
        elif axis == 'z':
            parallelepiped.rotate_z(angle)
        else:
            print("Невідома вісь. Спробуйте ще раз.")
            continue
        
        # Виводимо результат на екран
        grid = parallelepiped.draw(colored=True)
        for row in grid:
            print(''.join(row))

        # Після виведення запитуємо, чи зберегти арт у файл
        save = input("Зберегти арт у файл? (y/n): ")
        if save.lower() == 'y':
            filename = input("Введіть ім'я файлу (без розширення): ") + ".txt"
            parallelepiped.save_to_file(filename, parallelepiped.draw(colored=False))
            print(f"Арт збережено у файл: {filename}")
        
        cont = input("Обертати далі? (y/n): ")
        if cont.lower() == 'n':
            break

if __name__ == "__main__":
    main()
