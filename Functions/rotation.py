import math

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

   