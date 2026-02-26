import gulp from 'gulp';
import {
	srcFonts, srcImages, srcScripts, srcStyles, srcTemplates,
} from './consts.js';
import { bs } from './default.js';
import fonts from './fonts.js';
import images from './images.js';
import scripts from './scripts.js';
import stylesSass from './stylesSass.js';
import stylesStyl from './stylesStyl.js';
import svg from './svg.js';

const html = (cb) => {
	bs.reload();
	cb();
};

const watcher = () => {
	gulp.watch(`${srcFonts}/**`, fonts);
	gulp.watch(`${srcImages}/**`, images);
	gulp.watch(`${srcImages}/**/icon*.svg`, svg);
	gulp.watch(`${srcStyles}/**/*`, stylesStyl);
	gulp.watch(`${srcStyles}/**/*`, stylesSass);
	gulp.watch(`${srcScripts}/**/*`, scripts);
	gulp.watch(`${srcTemplates}/**/*`, html);
	gulp.watch('applications/**/templates/**/*', html);
};

export default watcher;
