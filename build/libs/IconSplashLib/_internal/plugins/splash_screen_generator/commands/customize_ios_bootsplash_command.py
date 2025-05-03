from plugins.splash_screen_generator.bootsplash import IOSCustomizer
import logging
from tqdm import tqdm

class CustomizeIOSBootsplashCommand:
    def __init__(self, ios_path, ios_project_name):
        self.ios_path = ios_path
        self.ios_project_name = ios_project_name
        self.progress_callback = None
        self.use_tqdm = False

    def set_progress_callback(self, callback):
        self.progress_callback = callback

    def execute(self):
        try:
            if self.use_tqdm:
                with tqdm(total=100, desc="Customizing iOS Bootsplash") as pbar:
                    IOSCustomizer.customize_bootsplash(self.ios_path, self.ios_project_name)
                    pbar.update(50)
                    if self.progress_callback:
                        self.progress_callback(50, "Customizing iOS Bootsplash")
                    IOSCustomizer.customize_launch_screen(self.ios_project_name)
                    pbar.update(50)
                    if self.progress_callback:
                        self.progress_callback(100, "Customizing Launch Screen")
            else:
                IOSCustomizer.customize_bootsplash(self.ios_path, self.ios_project_name)
                if self.progress_callback:
                    self.progress_callback(50, "Customizing iOS Bootsplash")
                IOSCustomizer.customize_launch_screen(self.ios_project_name)
                if self.progress_callback:
                    self.progress_callback(100, "Customizing Launch Screen")
        except Exception as e:
            logging.error(f"Error executing CustomizeIOSBootsplashCommand: {e}", exc_info=True)
