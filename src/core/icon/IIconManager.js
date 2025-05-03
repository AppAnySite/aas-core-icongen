/**
 * Interface for IconManager.
 * @interface
 */
class IIconManager {
  /**
   * Updates the app icon.
   * @param {string} projectDirectory - The project directory.
   * @param {string} iconPath - The path to the new app icon.
   */
  updateIcon(projectDirectory, iconPath) {
    throw new Error('Method not implemented');
  }
}

export default IIconManager;
