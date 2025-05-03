import IIconManager from './IIconManager';
import fs from 'fs';
import path from 'path';
import { spawn } from 'child_process';
import { log } from '../../utils/logger';
import { handleError } from '../../utils/errorHandler';
import chalk from 'chalk';
import os from 'os';

/**
 * IconManager class.
 * Manages updating the app icon for a React Native project.
 * @extends IIconManager
 */
class IconManager extends IIconManager {
  async updateIcon(projectDirectory, iconPath, platform, folder, iconType, suppressLogs = false) {
    try {
      const inputImagePath = path.resolve(iconPath);
      const projectPath = path.resolve(projectDirectory);
      let binaryPath;

      // Determine the binary path based on the operating system
      if (os.platform() === 'win32') {
        binaryPath = process.pkg ? 
          path.join(path.dirname(process.execPath), 'libs', 'IconSplashLib', 'IconSplashLib.exe') : 
          path.resolve(__dirname, '../../build/IconSplashLib/IconSplashLib.exe');
      } else {
        binaryPath = process.pkg ? 
          path.join(path.dirname(process.execPath), 'libs', 'IconSplashLib', 'IconSplashLib') : 
          path.resolve(__dirname, '../../build/IconSplashLib/IconSplashLib');
      }

      if (!fs.existsSync(binaryPath)) {
        log('ERROR', `Binary file not found: ${binaryPath}`, chalk.red);
        return;
      }

      const args = [projectPath, '--icon', inputImagePath];
      if (platform) args.push('--platform', platform);
      if (folder) args.push('--folder', folder);
      if (iconType) args.push('--icon-type', iconType);

      const child = spawn(binaryPath, args);

      if (!suppressLogs) {
        // Stream stdout and stderr to the terminal only if suppressLogs is false
        child.stdout.on('data', (data) => {
          process.stdout.write(data);
        });

        child.stderr.on('data', (data) => {
          process.stderr.write(data);
        });
      }

      child.on('close', (code) => {
        if (code === 0) {
          log('INFO', 'Icon update completed successfully', chalk.green);
        } else {
          log('ERROR', `Binary process exited with code ${code}`, chalk.red);
        }
      });

    } catch (error) {
      handleError(error);
    }
  }
}

export default IconManager;
