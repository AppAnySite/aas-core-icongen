import os

class AndroidCustomizer:
    @staticmethod
    def customize_styles(android_path):
        styles_path = os.path.join(android_path, "app", "src", "main", "res", "values", "styles.xml")

        with open(styles_path, 'r') as file:
            content = file.read()

        if "<style name=\"BootTheme\"" not in content:
            insert_position = content.rfind("</resources>")
            if insert_position == -1:
                raise ValueError("The styles.xml file is missing the closing </resources> tag.")

            boot_theme_style = """
    <style name="BootTheme" parent="Theme.BootSplash">
      <item name="bootSplashBackground">@color/bootsplash_background</item>
      <item name="bootSplashLogo">@drawable/bootsplash_logo</item>
      <item name="postBootSplashTheme">@style/AppTheme</item>
    </style>
"""
            content = content[:insert_position] + boot_theme_style + content[insert_position:]

            with open(styles_path, 'w') as file:
                file.write(content)

    @staticmethod
    def customize_manifest(android_path):
        manifest_path = os.path.join(android_path, "app", "src", "main", "AndroidManifest.xml")

        with open(manifest_path, 'r+') as file:
            content = file.read()

            if 'android:theme="@style/BootTheme"' not in content:
                content = content.replace(
                    'android:exported="true"',
                    'android:exported="true"\n        android:theme="@style/BootTheme"'
                )

            file.seek(0)
            file.write(content)
            file.truncate()

    @staticmethod
    def customize_main_activity(android_path, android_project_name):
        main_activity_path = os.path.join(android_path, "app", "src", "main", "java", "com", android_project_name.lower(), "MainActivity.kt")

        with open(main_activity_path, 'r+') as file:
            content = file.read()

            if 'import android.os.Bundle' not in content:
                content = content.replace(
                    'import com.facebook.react.defaults.DefaultReactActivityDelegate',
                    'import com.facebook.react.defaults.DefaultReactActivityDelegate\nimport android.os.Bundle\nimport com.zoontek.rnbootsplash.RNBootSplash'
                )

            if 'override fun onCreate(savedInstanceState: Bundle?)' not in content:
                insert_position = content.find('class MainActivity : ReactActivity() {') + len('class MainActivity : ReactActivity() {\n')
                on_create_method = """
  override fun onCreate(savedInstanceState: Bundle?) {
    RNBootSplash.init(this, R.style.BootTheme)
    super.onCreate(savedInstanceState)
  }
"""
                content = content[:insert_position] + on_create_method + content[insert_position:]

            file.seek(0)
            file.write(content)
            file.truncate()
