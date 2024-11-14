
def save_to_file(self, filename, grid):
        """Зберігає ASCII-арт у текстовий файл"""
        with open(filename, 'w') as file:
            for row in grid:
                file.write(''.join(row) + '\n')