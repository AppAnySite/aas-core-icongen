# AppAnySite Mobile App Icon Creation and Testing

## Table of Contents
1. [Generating Icons and Splash Screen](#generating-icons-using-aas-core-icongen-with-iconsplashlib-library)
2. [Testing the Application - Mobile](#testing-the-application---mobile)

### Generating Icons using aas-core-icongen with IconSplashLib Library

To create a mobile app project, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/AppAnySite/aas-core-icongen.git
    ```

2. Navigate to the CLI tool directory:
    ```bash
    cd aas-core-icongen
    ```

3. Install the necessary npm packages:
    ```bash
    npm install
    npm install -g @vercel/ncc
    npm install -g pkg


4. Build the project using `ncc`:
    ```bash
    ncc build index.js -o bin/lib
    ```

5. Package the project for the desired target:
    ```bash
    pkg bin/lib/index.js --target node16-macos-arm64 --output build/ICONGEN # MacOSX
    pkg bin/lib/index.js --target node16-win-x64 --output build/ICONGEN # Windows
    ```

6. Update the icon in your project:
    ```bash
    ./build/ICONGEN update-icon --directory CREATED_PROJECT_DIRECTORY --icon PNG_IMAGE_PATH
    ```



## Testing the Application - Mobile

To test the mobile application, follow these steps:

1. Navigate to your project directory:
    ```bash
    cd CREATED_PROJECT_DIRECTORY_PATH
    ```

2. Run the application on Android:
    ```bash
    npx react-native run-android
    ```

3. Run the application on iOS:
    ```bash
    npx react-native run-ios
    ```
