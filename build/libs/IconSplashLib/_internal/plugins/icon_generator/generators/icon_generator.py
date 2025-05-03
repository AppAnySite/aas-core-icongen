from abc import ABC, abstractmethod

class IconGenerator(ABC):
    def __init__(self, input_image_path, output_directory, config):
        self.input_image_path = input_image_path
        self.output_directory = output_directory
        self.config = config

    @abstractmethod
    def generate_icons(self):
        pass
