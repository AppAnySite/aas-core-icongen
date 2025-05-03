import os
import subprocess

class IOSCustomizer:
    @staticmethod
    def customize_bootsplash(ios_path, ios_project_name):
        app_delegate_path = os.path.join(ios_path, "AppDelegate.mm")
        if not os.path.isfile(app_delegate_path):
            print(f"Error: {app_delegate_path} does not exist.")
            return

        with open(app_delegate_path, 'r+') as file:
            content = file.read()

            if "#import \"RNBootSplash.h\"" not in content:
                content = content.replace(
                    "#import <React/RCTBundleURLProvider.h>",
                    "#import <React/RCTBundleURLProvider.h>\n#import \"RNBootSplash.h\""
                )

            if "- (void)customizeRootView:(RCTRootView *)rootView {" not in content:
                content = content.replace(
                    "@end",
                    "\n- (void)customizeRootView:(RCTRootView *)rootView {\n  [RNBootSplash initWithStoryboard:@\"BootSplash\" rootView:rootView];\n}\n@end"
                )

            file.seek(0)
            file.write(content)
            file.truncate()

    @staticmethod
    def customize_launch_screen(ios_project_name):
        plist_path = os.path.join("ios", ios_project_name, "Info.plist")
        subprocess.run(["/usr/libexec/PlistBuddy", "-c", "Set :UILaunchStoryboardName BootSplash", plist_path], check=True)
