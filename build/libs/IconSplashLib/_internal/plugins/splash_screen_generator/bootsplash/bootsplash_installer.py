import subprocess
import os

class BootsplashInstaller:
    @staticmethod
    def install_dependencies(project_path):
        os.chdir(project_path)
        subprocess.run(
            ["npm", "install", "--save", "react-native-bootsplash"], 
            check=True,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

    @staticmethod
    def generate(logo_path):
        subprocess.run(
            [
                "npx", "react-native", "generate-bootsplash", logo_path,
                "--platforms=android,ios",
                "--background=F5FCFF",
                "--logo-width=100",
                "--assets-output=assets",
                "--flavor=main",
                "--html=index.html"
            ], 
            check=True,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
