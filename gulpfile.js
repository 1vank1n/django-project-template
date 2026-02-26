import gulp from 'gulp';
import clean from './tasks/clean.js';
import { isBuild } from './tasks/consts.js';
import bsTask from './tasks/default.js';
import fonts from './tasks/fonts.js';
import images from './tasks/images.js';
import scripts from './tasks/scripts.js';
import stylesSass from './tasks/stylesSass.js';
import stylesStyl from './tasks/stylesStyl.js';
import svg from './tasks/svg.js';
import watcher from './tasks/watch.js';

const { parallel, series } = gulp;

const buildSeries = [
	clean,
	parallel(
		fonts,
		stylesSass,
		stylesStyl,
		scripts,
		images,
		svg,
	),
];

const watchSeries = [
	parallel(
		bsTask,
		watcher,
	),
];

export default isBuild
	? series(...buildSeries)
	: series(...buildSeries, ...watchSeries);
