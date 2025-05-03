import UpdateIconCommand from './modules/updateIcon/UpdateIconCommand';
import UpdateIconCommandValidator from './modules/updateIcon/validators/UpdateIconCommandValidator';
import IconManager from './core/icon/IconManager';
import ErrorHandler from './utils/errorHandler';

class DIContainer {
  constructor() {
    this.services = {};
  }

  register(name, Constructor, dependencies = []) {
    if (typeof Constructor !== 'function') {
      throw new Error(`Constructor for ${name} is not a function`);
    }
    this.services[name] = { Constructor, dependencies };
  }

  get(name) {
    const service = this.services[name];
    if (!service) {
      throw new Error(`Service ${name} not found`);
    }
    const { Constructor, dependencies } = service;
    const resolvedDependencies = dependencies.map(dep => this.get(dep));
    return new Constructor(...resolvedDependencies);
  }
}

const container = new DIContainer();

// Registering all services with their dependencies
container.register('UpdateIconCommand', UpdateIconCommand, ['UpdateIconCommandValidator', 'IconManager', 'ErrorHandler']);
container.register('UpdateIconCommandValidator', UpdateIconCommandValidator);
container.register('IconManager', IconManager);
container.register('ErrorHandler', ErrorHandler);


export default container;
