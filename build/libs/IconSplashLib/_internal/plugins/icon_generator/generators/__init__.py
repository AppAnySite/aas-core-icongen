from .android_icon_generator import AndroidIconGenerator
from .ios_icon_generator import IOSIconGenerator

class IconGeneratorFactory:
    @staticmethod
    def create_icon_generator(platform, input_image_path, output_directory, config, sizes=None, folders=None, icon_type=None):
        if platform == 'android':
            return AndroidIconGenerator(input_image_path, output_directory, config, sizes, folders, icon_type)
        elif platform == 'ios':
            return IOSIconGenerator(input_image_path, output_directory, config, sizes, folders)
        else:
            raise ValueError(f"Unsupported platform: {platform}")
