from plugins.icon_generator.generators import IconGeneratorFactory
from tqdm import tqdm
import logging

class GenerateIconsCommand:
    def __init__(self, platform, input_image_path, output_directory, config, sizes=None, folders=None, icon_type=None):
        self.platform = platform
        self.input_image_path = input_image_path
        self.output_directory = output_directory
        self.config = config
        self.sizes = sizes
        self.folders = folders
        self.icon_type = icon_type
        self.use_tqdm = False  # Default to not using tqdm
        self.progress_callback = None

    def set_progress_callback(self, callback):
        self.progress_callback = callback

    def execute(self):
        try:
            generator = IconGeneratorFactory.create_icon_generator(
                self.platform, self.input_image_path, self.output_directory, self.config, self.sizes, self.folders, self.icon_type
            )

            # Calculate the total number of icons to be generated dynamically
            total_tasks = 0
            if self.platform == 'android':
                for folder, icons in self.config["icon_sizes"].items():
                    if self.folders and folder not in self.folders:
                        continue  # Skip folders not specified
                    if self.icon_type:
                        if self.icon_type in icons:
                            total_tasks += 1
                    else:
                        total_tasks += len(icons)
            elif self.platform == 'ios':
                for folder, size in self.config["icon_sizes"].items():
                    if self.folders and folder not in self.folders:
                        continue  # Skip folders not specified
                    total_tasks += 1

            if total_tasks == 0:
                logging.info("No tasks to execute based on the provided parameters.")
                return

            completed_tasks = 0

            # Conditional tqdm usage
            if self.use_tqdm:
                progress_bar = tqdm(total=total_tasks, desc="Progress", unit="icon")
            else:
                progress_bar = None

            for task in generator.generate_icons():
                completed_tasks += 1
                progress = round((completed_tasks / total_tasks) * 100)  # Ensure integer progress values
                if self.use_tqdm:
                    progress_bar.update(1)
                if self.progress_callback:
                    self.progress_callback(progress, task)
            
            if self.use_tqdm:
                progress_bar.n = progress_bar.total  # Ensure progress bar reaches 100% at the end
                progress_bar.refresh()  # Update the progress bar to show 100%
                progress_bar.close()

            if self.platform == 'ios':
                generator.generate_contents_json()
        except Exception as e:
            logging.error(f"Error executing GenerateIconsCommand: {e}", exc_info=True)
