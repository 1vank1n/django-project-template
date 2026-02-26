import gulp from 'gulp';
import { distFonts, srcFonts } from './consts.js';

const fonts = () => gulp.src(`${srcFonts}/*`)
	.pipe(gulp.dest(distFonts));

export default fonts;
