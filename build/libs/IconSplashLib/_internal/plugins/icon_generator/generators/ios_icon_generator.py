import os
from PIL import Image
import json
import logging
from .icon_generator import IconGenerator

class IOSIconGenerator(IconGenerator):
    def __init__(self, input_image_path, output_directory, config, custom_sizes=None, folders=None):
        super().__init__(input_image_path, output_directory, config)
        self.icon_sizes = config["icon_sizes"]
        self.custom_sizes = custom_sizes
        self.folders = folders

    def generate_icons(self):
        try:
            os.makedirs(self.output_directory, exist_ok=True)
            with Image.open(self.input_image_path) as img:
                if self.custom_sizes:
                    for size in self.custom_sizes:
                        output_path = os.path.join(self.output_directory, f"icon_{size[0]}x{size[1]}.png")
                        logging.info(f"Generating custom icon: {output_path} with size {size}")
                        img.resize(size, Image.LANCZOS).save(output_path, "PNG")
                        logging.info(f"Saved custom icon: {output_path}")
                        yield f"Generated custom icon {output_path}"
                else:
                    for name, size in self.icon_sizes.items():
                        if self.folders and name not in self.folders:
                            continue
                        # logging.info(f"Generating iOS icon: {name} with size {size}")
                        resized_img = img.resize(size, Image.LANCZOS)
                        output_path = os.path.join(self.output_directory, f"{name}.png")
                        resized_img.save(output_path, "PNG")
                        # logging.info(f"Saved iOS icon: {output_path}")
                        yield f"Generated icon {output_path}"
        except Exception as e:
            logging.error(f"Error generating iOS icons: {e}", exc_info=True)
            yield f"Error generating icon: {e}"

    def generate_contents_json(self):
        try:
            contents = {
                "images": [
                    {"idiom": "iphone", "scale": "2x", "size": "20x20", "filename": "AppIcon-20x20@2x.png"},
                    {"idiom": "iphone", "scale": "3x", "size": "20x20", "filename": "AppIcon-20x20@3x.png"},
                    {"idiom": "iphone", "scale": "2x", "size": "29x29", "filename": "AppIcon-29x29@2x.png"},
                    {"idiom": "iphone", "scale": "3x", "size": "29x29", "filename": "AppIcon-29x29@3x.png"},
                    {"idiom": "iphone", "scale": "2x", "size": "40x40", "filename": "AppIcon-40x40@2x.png"},
                    {"idiom": "iphone", "scale": "3x", "size": "40x40", "filename": "AppIcon-40x40@3x.png"},
                    {"idiom": "iphone", "scale": "2x", "size": "60x60", "filename": "AppIcon-60x60@2x.png"},
                    {"idiom": "iphone", "scale": "3x", "size": "60x60", "filename": "AppIcon-60x60@3x.png"},
                    {"idiom": "ios-marketing", "scale": "1x", "size": "1024x1024", "filename": "AppIcon-1024x1024@1x.png"}
                ],
                "info": {"author": "xcode", "version": 1}
            }
            contents_json_path = os.path.join(self.output_directory, "Contents.json")
            with open(contents_json_path, 'w') as f:
                json.dump(contents, f, indent=4)
            # logging.info(f"Generated Contents.json at {contents_json_path}")
        except Exception as e:
            logging.error(f"Error generating Contents.json: {e}", exc_info=True)
