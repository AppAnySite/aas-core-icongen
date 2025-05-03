import os

class ProjectUtils:
    @staticmethod
    def find_ios_project_name(ios_path):
        """Find the iOS project name in the specified path."""
        for item in os.listdir(ios_path):
            if item.endswith(".xcodeproj"):
                return item.split(".")[0]
        return None
