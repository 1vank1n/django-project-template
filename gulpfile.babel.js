import { series, parallel } from 'gulp';
import clean from './tasks/clean';
import fonts from './tasks/fonts';
import styles from './tasks/styles';
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
		styles,
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
