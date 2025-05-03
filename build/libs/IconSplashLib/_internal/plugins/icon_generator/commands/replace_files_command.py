from plugins.icon_generator.replacers import AndroidFileReplacer, IOSFileReplacer
import logging

class ReplaceFilesCommand:
    def __init__(self, platform, project_path, generated_path, ios_project_name=None):
        self.platform = platform
        self.project_path = project_path
        self.generated_path = generated_path
        self.ios_project_name = ios_project_name
        self.progress_callback = None

    def set_progress_callback(self, callback):
        self.progress_callback = callback

    def execute(self):
        try:
            logging.info(f"Executing ReplaceFilesCommand for {self.platform}")
            replacer = None
            if self.platform == 'android':
                replacer = AndroidFileReplacer()
            elif self.platform == 'ios':
                replacer = IOSFileReplacer(self.ios_project_name)

            if replacer:
                replacer.replace(self.project_path, self.generated_path)
                if self.progress_callback:
                    self.progress_callback(100, f"Replacing Files for {self.platform}")

            logging.info(f"Successfully replaced files for {self.platform}")
        except Exception as e:
            logging.error(f"Error executing ReplaceFilesCommand: {e}", exc_info=True)
