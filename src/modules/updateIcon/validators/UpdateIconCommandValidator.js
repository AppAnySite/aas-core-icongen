import IUpdateIconCommandValidator from './IUpdateIconCommandValidator';

/**
 * UpdateIconCommandValidator class.
 * Validates the options for updating the app icon.
 * @extends IUpdateIconCommandValidator
 */
class UpdateIconCommandValidator extends IUpdateIconCommandValidator {
  /**
   * Validates the options.
   * @param {Object} options - Options to validate.
   * @throws Will throw an error if validation fails.
   */
  validate(options) {
    if (!options.directory) {
      throw new Error('Project directory is required.');
    }
    if (!options.icon) {
      throw new Error('Icon path is required.');
    }
  }
}

export default UpdateIconCommandValidator;
