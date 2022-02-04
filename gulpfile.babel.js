import { parallel, series } from 'gulp';
import ckeditor from './tasks/ckeditor';
import clean from './tasks/clean';
import { isBuild } from './tasks/consts';
import bsTask from './tasks/default';
import fonts from './tasks/fonts';
import images from './tasks/images';
import scripts from './tasks/scripts';
import scriptsVendor from './tasks/scriptsVendor';
import stylesSass from './tasks/stylesSass';
import stylesStyl from './tasks/stylesStyl';
import svg from './tasks/svg';
import watcher from './tasks/watch';

const buildSeries = [
	clean,
	parallel(
		fonts,
		stylesSass,
		stylesStyl,
		scriptsVendor,
		scripts,
		images,
		svg,
		ckeditor,
	),
];

const watchSeries = [
	parallel(
		bsTask,
		watcher,
	),
];

exports.default = isBuild
	? series(...buildSeries)
	: series(...buildSeries, ...watchSeries);
