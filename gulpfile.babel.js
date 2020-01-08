import { series, parallel } from 'gulp';
import clean from './tasks/clean';
import fonts from './tasks/fonts';
import stylesSass from './tasks/stylesSass';
import stylesStyl from './tasks/stylesStyl';
import bsTask from './tasks/default';
import scriptsVendor from './tasks/scriptsVendor';
import scripts from './tasks/scripts';
import images from './tasks/images';
import svg from './tasks/svg';
import watcher from './tasks/watch';

exports.default = series(
	clean,
	parallel(
		fonts,
		stylesSass,
		stylesStyl,
		scriptsVendor,
		scripts,
		images,
		svg,
	),
	parallel(
		bsTask,
		watcher,
	),
);
