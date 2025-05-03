import os
import shutil
import logging
from .file_replacer import FileReplacer

class IOSFileReplacer(FileReplacer):
    def __init__(self, ios_project_name):
        self.ios_project_name = ios_project_name

    def replace(self, project_path, generated_path):
        try:
            logging.info(f"Replacing iOS icons from {generated_path} to {project_path}")
            appiconset_path = os.path.join(project_path, "ios", self.ios_project_name, "Images.xcassets", "AppIcon.appiconset")
            if os.path.exists(appiconset_path):
                for root, _, files in os.walk(generated_path):
                    for filename in files:
                        src_file = os.path.join(root, filename)
                        dst_file = os.path.join(appiconset_path, filename)
                        if os.path.exists(dst_file):
                            os.remove(dst_file)
                        shutil.copy(src_file, dst_file)
            else:
                shutil.copytree(generated_path, appiconset_path)
            logging.info("iOS icons replaced successfully")
        except Exception as e:
            logging.error(f"Error replacing iOS icons: {e}", exc_info=True)
