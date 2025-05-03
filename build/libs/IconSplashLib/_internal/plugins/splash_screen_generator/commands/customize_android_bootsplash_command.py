from plugins.splash_screen_generator.bootsplash import AndroidCustomizer
import logging
from tqdm import tqdm

class CustomizeAndroidBootsplashCommand:
    def __init__(self, android_path, android_project_name):
        self.android_path = android_path
        self.android_project_name = android_project_name
        self.progress_callback = None
        self.use_tqdm = False

    def set_progress_callback(self, callback):
        self.progress_callback = callback

    def execute(self):
        try:
            if self.use_tqdm:
                with tqdm(total=100, desc="Customizing Android Bootsplash") as pbar:
                    AndroidCustomizer.customize_styles(self.android_path)
                    pbar.update(33)
                    if self.progress_callback:
                        self.progress_callback(33, "Customizing Android Styles")
                    AndroidCustomizer.customize_manifest(self.android_path)
                    pbar.update(33)
                    if self.progress_callback:
                        self.progress_callback(66, "Customizing Android Manifest")
                    AndroidCustomizer.customize_main_activity(self.android_path, self.android_project_name)
                    pbar.update(34)
                    if self.progress_callback:
                        self.progress_callback(100, "Customizing Android MainActivity")
            else:
                AndroidCustomizer.customize_styles(self.android_path)
                if self.progress_callback:
                    self.progress_callback(33, "Customizing Android Styles")
                AndroidCustomizer.customize_manifest(self.android_path)
                if self.progress_callback:
                    self.progress_callback(66, "Customizing Android Manifest")
                AndroidCustomizer.customize_main_activity(self.android_path, self.android_project_name)
                if self.progress_callback:
                    self.progress_callback(100, "Customizing Android MainActivity")
        except Exception as e:
            logging.error(f"Error executing CustomizeAndroidBootsplashCommand: {e}", exc_info=True)
