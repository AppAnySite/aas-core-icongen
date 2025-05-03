import IUpdateIconCommand from './IUpdateIconCommand';
import { handleError } from '../../utils/errorHandler';
import { log } from '../../utils/logger';

/**
 * UpdateIconCommand class.
 * Handles the updating of the app icon.
 * @extends IUpdateIconCommand
 */
class UpdateIconCommand extends IUpdateIconCommand {
  constructor(updateIconCommandValidator, iconManager, errorHandler) {
    super();
    this.updateIconCommandValidator = updateIconCommandValidator;
    this.iconManager = iconManager;
    this.errorHandler = errorHandler;
  }

  async execute(options) {
    try {
      this.updateIconCommandValidator.validate(options);

      // If no platform is specified, update for both Android and iOS
      if (!options.platform) {
        log('INFO', 'No platform specified, updating icon for both Android and iOS');
        await this.iconManager.updateIcon(options.directory, options.icon, 'android', undefined, undefined, false);  // Logs should be printed
        await this.iconManager.updateIcon(options.directory, options.icon, 'ios', undefined, undefined, false);      // Logs should be printed
      } else {
        // Update for the specified platform
        await this.iconManager.updateIcon(options.directory, options.icon, options.platform, undefined, undefined, false);  // Logs should be printed
      }

    } catch (error) {
      this.errorHandler.handleError(error);
    }
  }
}

export default UpdateIconCommand;
