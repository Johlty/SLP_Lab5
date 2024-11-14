from Functions.vertices_creator import create_vertices

class Parallelepiped3D:
    def __init__(self, length, width, height, color, console_color):
        self.length = length
        self.width = width
        self.height = height
        self.color = color  # Символ без кольору для файлу
        self.console_color = console_color  # Кольоровий символ для консолі
        self.vertices = self.create_vertices()

   