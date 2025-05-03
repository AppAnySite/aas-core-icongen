/**
 * Interface for UpdateIconCommand.
 * @interface
 */
class IUpdateIconCommand {
  /**
   * Executes the command to update the app icon.
   * @param {Object} options - Options for updating the icon.
   */
  execute(options) {
    throw new Error('Method not implemented');
  }
}

export default IUpdateIconCommand;
