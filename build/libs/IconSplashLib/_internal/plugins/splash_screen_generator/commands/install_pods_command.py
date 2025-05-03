import subprocess
import logging
from tqdm import tqdm

class InstallPodsCommand:
    def __init__(self):
        self.progress_callback = None
        self.use_tqdm = False

    def set_progress_callback(self, callback):
        self.progress_callback = callback

    def execute(self):
        try:
            if self.use_tqdm:
                with tqdm(total=100, desc="Installing Pods") as pbar:
                    subprocess.run(
                        ["npx", "pod-install"], 
                        check=True, 
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE
                    )
                    pbar.update(100)
                    if self.progress_callback:
                        self.progress_callback(100, "Installing Pods")
            else:
                subprocess.run(
                    ["npx", "pod-install"], 
                    check=True, 
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE
                )
                if self.progress_callback:
                    self.progress_callback(100, "Installing Pods")
        except subprocess.CalledProcessError as e:
            logging.error(f"Error executing InstallPodsCommand: {e}", exc_info=True)
