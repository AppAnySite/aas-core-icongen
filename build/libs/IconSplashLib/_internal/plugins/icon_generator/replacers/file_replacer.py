from abc import ABC, abstractmethod

class FileReplacer(ABC):
    @abstractmethod
    def replace(self, project_path, generated_path):
        pass
