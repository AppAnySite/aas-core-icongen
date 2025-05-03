#!/usr/bin/env node

import { Command } from 'commander';
import chalk from 'chalk';
import { log } from './utils/logger';
import container from './diContainer';


const program = new Command();



  program
  .command('update-icon')
  .description('Update the app icon')
  .requiredOption('-d, --directory <projectDirectory>', 'Directory where the project is located')
  .requiredOption('-i, --icon <icon>', 'Path to the new app icon')
  .option('--platform <platform>', 'Specify platform (android, ios)')
  .option('--folder <folder>', 'Specify the folder (e.g., mipmap-mdpi)')
  .option('--icon-type <iconType>', 'Specify the icon type (e.g., round)')
  .action((options) => {
    const updateIconCommand = container.get('UpdateIconCommand');
    updateIconCommand.execute(options);
  });


program.parse(process.argv);
