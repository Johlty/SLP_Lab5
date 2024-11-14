from Class.Figure import Parallelepiped3D

def create_vertices(self):
        """Створюємо 8 вершин паралелепіпеда"""
        l = self.length / 4
        w = self.width / 4
        h = self.height / 4
        return [
            [-l, -w, -h], [l, -w, -h], [l, w, -h], [-l, w, -h],  # Задня грань
            [-l, -w, h], [l, -w, h], [l, w, h], [-l, w, h]       # Передня грань
        ]
