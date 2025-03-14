# Esto es una libreria, para abrir, guardar y eliminar archivos de texto en el sistema.

import os

class FileManager:
    def __init__(self, file_path=None):
        self.file_path = file_path

    def open_file(self):
        if self.file_path and os.path.exists(self.file_path):
            with open(self.file_path, "r", encoding="utf-8") as file:
                return file.read()
        raise FileNotFoundError("El archivo no existe")

    def save_file(self, content):
        if not self.file_path:
            raise ValueError("No se ha especificado un archivo")
        with open(self.file_path, "w", encoding="utf-8") as file:
            file.write(content)

    def delete_file(self):
        if self.file_path and os.path.exists(self.file_path):
            os.remove(self.file_path)
        else:
            raise FileNotFoundError("El archivo no existe")