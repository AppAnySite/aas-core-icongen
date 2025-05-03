from plugins.splash_screen_generator.bootsplash import BootsplashInstaller
import logging
from tqdm import tqdm

class GenerateBootsplashCommand:
    def __init__(self, project_path, logo_path):
        self.project_path = project_path
        self.logo_path = logo_path
        self.progress_callback = None
        self.use_tqdm = False

    def set_progress_callback(self, callback):
        self.progress_callback = callback

    def execute(self):
        try:
            if self.use_tqdm:
                with tqdm(total=100, desc="Generating Bootsplash") as pbar:
                    BootsplashInstaller.install_dependencies(self.project_path)
                    pbar.update(50)
                    if self.progress_callback:
                        self.progress_callback(50, "Dependencies Installed")
                    BootsplashInstaller.generate(self.logo_path)
                    pbar.update(50)
                    if self.progress_callback:
                        self.progress_callback(100, "Bootsplash Generated")
            else:
                BootsplashInstaller.install_dependencies(self.project_path)
                if self.progress_callback:
                    self.progress_callback(50, "Dependencies Installed")
                BootsplashInstaller.generate(self.logo_path)
                if self.progress_callback:
                    self.progress_callback(100, "Bootsplash Generated")
        except Exception as e:
            logging.error(f"Error executing GenerateBootsplashCommand: {e}", exc_info=True)
