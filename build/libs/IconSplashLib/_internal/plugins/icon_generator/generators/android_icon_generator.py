import os
from PIL import Image, ImageDraw, ImageOps
import logging
from .icon_generator import IconGenerator

class AndroidIconGenerator(IconGenerator):
    def __init__(self, input_image_path, output_directory, config, custom_sizes=None, folders=None, icon_type=None):
        super().__init__(input_image_path, output_directory, config)
        self.icon_sizes = config["icon_sizes"]
        self.custom_sizes = custom_sizes
        self.folders = folders
        self.icon_type = icon_type

    def generate_icon(self, img, size, output_path):
        resized_img = img.resize((size, size), Image.LANCZOS)
        resized_img.save(output_path, "PNG")

    def generate_round_icon(self, img, size, output_path):
        mask = Image.new("L", (size, size), 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0, size, size), fill=255)
        rounded_img = ImageOps.fit(img, mask.size, centering=(0.5, 0.5))
        rounded_img.putalpha(mask)
        rounded_img.save(output_path, "PNG")

    def generate_icons(self):
        try:
            os.makedirs(self.output_directory, exist_ok=True)
            with Image.open(self.input_image_path) as img:
                tasks = []
                if self.custom_sizes:
                    for size in self.custom_sizes:
                        output_path = os.path.join(self.output_directory, f"icon_{size[0]}x{size[1]}.png")
                        self.generate_icon(img, size[0], output_path)
                        tasks.append(output_path)
                        yield f"Generated custom icon {output_path}"
                else:
                    total_icons = sum(len(icons) for icons in self.icon_sizes.values())
                    for directory, icons in self.icon_sizes.items():
                        if self.folders:
                            for folder in self.folders:
                                if directory == folder:
                                    density_directory = os.path.join(self.output_directory, directory)
                                    os.makedirs(density_directory, exist_ok=True)
                                    for icon_type, (size, filename) in icons.items():
                                        if self.icon_type and self.icon_type != icon_type:
                                            continue
                                        output_path = os.path.join(density_directory, filename)
                                        if icon_type == "round":
                                            self.generate_round_icon(img, size, output_path)
                                        else:
                                            self.generate_icon(img, size, output_path)
                                        tasks.append(output_path)
                                        yield f"Generated icon {output_path}"
                        else:
                            density_directory = os.path.join(self.output_directory, directory)
                            os.makedirs(density_directory, exist_ok=True)
                            for icon_type, (size, filename) in icons.items():
                                if self.icon_type and self.icon_type != icon_type:
                                    continue
                                output_path = os.path.join(density_directory, filename)
                                if icon_type == "round":
                                    self.generate_round_icon(img, size, output_path)
                                else:
                                    self.generate_icon(img, size, output_path)
                                tasks.append(output_path)
                                yield f"Generated icon {output_path}"

            return tasks
        except Exception as e:
            logging.error(f"Error generating Android icons: {e}", exc_info=True)
