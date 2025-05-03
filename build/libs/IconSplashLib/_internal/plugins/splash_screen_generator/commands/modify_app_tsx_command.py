import logging
import os
from tqdm import tqdm

class ModifyAppTSXCommand:
    def __init__(self, app_tsx_path):
        self.app_tsx_path = app_tsx_path
        self.progress_callback = None
        self.use_tqdm = False

    def set_progress_callback(self, callback):
        self.progress_callback = callback

    def execute(self):
        try:
            if not os.path.isfile(self.app_tsx_path):
                logging.error(f"App.tsx file not found at {self.app_tsx_path}")
                return

            with open(self.app_tsx_path, 'r') as file:
                lines = file.readlines()

            if self.use_tqdm:
                with tqdm(total=100, desc="Modifying App.tsx") as pbar:
                    for i, line in enumerate(lines):
                        if line.strip() == "import React from 'react';":
                            lines[i] = "import React, { useEffect } from 'react';\n"
                            break
                    pbar.update(30)
                    if self.progress_callback:
                        self.progress_callback(30, "Updated React import in App.tsx")

                    bootsplash_import_line = 'import BootSplash from "react-native-bootsplash";\n'
                    if bootsplash_import_line not in lines:
                        import_index = next((i for i, line in enumerate(lines) if line.startswith("import")), len(lines))
                        lines.insert(import_index + 1, bootsplash_import_line)
                    pbar.update(30)
                    if self.progress_callback:
                        self.progress_callback(60, "Added BootSplash import in App.tsx")

                    if not any("BootSplash.hide" in line for line in lines):
                        website_url_index = next((i for i, line in enumerate(lines) if "const websiteUrl" in line), len(lines))

                        useEffect_code = """
  useEffect(() => {
    const init = async () => {
      // …do multiple sync or async tasks
    };

    init().finally(async () => {
      await BootSplash.hide({ fade: true });
      console.log("BootSplash has been hidden successfully");
    });
  }, []);
"""
                        lines.insert(website_url_index + 1, useEffect_code)
                    pbar.update(30)
                    if self.progress_callback:
                        self.progress_callback(90, "Added useEffect in App.tsx")

            else:
                for i, line in enumerate(lines):
                    if line.strip() == "import React from 'react';":
                        lines[i] = "import React, { useEffect } from 'react';\n"
                        break
                if self.progress_callback:
                    self.progress_callback(30, "Updated React import in App.tsx")

                bootsplash_import_line = 'import BootSplash from "react-native-bootsplash";\n'
                if bootsplash_import_line not in lines:
                    import_index = next((i for i, line in enumerate(lines) if line.startswith("import")), len(lines))
                    lines.insert(import_index + 1, bootsplash_import_line)
                if self.progress_callback:
                    self.progress_callback(60, "Added BootSplash import in App.tsx")

                if not any("BootSplash.hide" in line for line in lines):
                    website_url_index = next((i for i, line in enumerate(lines) if "const websiteUrl" in line), len(lines))

                    useEffect_code = """
  useEffect(() => {
    const init = async () => {
      // …do multiple sync or async tasks
    };

    init().finally(async () => {
      await BootSplash.hide({ fade: true });
      console.log("BootSplash has been hidden successfully");
    });
  }, []);
"""
                    lines.insert(website_url_index + 1, useEffect_code)
                if self.progress_callback:
                    self.progress_callback(90, "Added useEffect in App.tsx")

            with open(self.app_tsx_path, 'w') as file:
                file.writelines(lines)
                if self.progress_callback:
                    self.progress_callback(100, "Finished modifying App.tsx")

        except Exception as e:
            logging.error(f"Error executing ModifyAppTSXCommand: {e}", exc_info=True)
