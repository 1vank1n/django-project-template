import gulp from 'gulp';
import { distImages, srcImages } from './consts.js';

const images = () => gulp.src([`${srcImages}/**`, `!${srcImages}/*/icon*.svg`])
	.pipe(gulp.dest(distImages));

export default images;
