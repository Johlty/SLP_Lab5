def project_vertex(self, vertex):
        """Проектуємо вершину 3D у 2D"""
        distance = 5  # Відстань до спостерігача
        factor = distance / (distance + vertex[2])
        
        # Масштабування не прив'язане до фіксованого полотна
        x_proj = int(vertex[0] * factor * 10)
        y_proj = int(vertex[1] * factor * 10)
        return (x_proj, y_proj)