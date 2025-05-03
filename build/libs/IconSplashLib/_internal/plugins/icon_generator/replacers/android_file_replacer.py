import os
import shutil
import logging
from .file_replacer import FileReplacer

class AndroidFileReplacer(FileReplacer):
    def replace(self, project_path, generated_path):
        try:
            logging.info(f"Replacing Android icons from {generated_path} to {project_path}")
            res_path = os.path.join(project_path, "android", "app", "src", "main", "res")
            for item in os.listdir(generated_path):
                if item.startswith("mipmap"):
                    src_folder = os.path.join(generated_path, item)
                    dst_folder = os.path.join(res_path, item)
                    if os.path.exists(dst_folder):
                        for filename in os.listdir(src_folder):
                            src_file = os.path.join(src_folder, filename)
                            dst_file = os.path.join(dst_folder, filename)
                            if os.path.exists(dst_file):
                                os.remove(dst_file)
                            shutil.copy(src_file, dst_file)
                    else:
                        shutil.copytree(src_folder, dst_folder)
            logging.info("Android icons replaced successfully")
        except Exception as e:
            logging.error(f"Error replacing Android icons: {e}", exc_info=True)
