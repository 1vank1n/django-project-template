import gulp from 'gulp';
import babel from 'gulp-babel';
import concat from 'gulp-concat';
import { distScripts, isDevelopment, srcScripts } from './consts.js';
import { bs } from './default.js';

const scripts = () => gulp.src(`${srcScripts}/*.js`, {
	sourcemaps: isDevelopment,
})
	.pipe(babel({ presets: ['@babel/env'] }))
	.pipe(concat('base.js'))
	.pipe(gulp.dest(distScripts, { sourcemaps: isDevelopment ? '.' : false }))
	.pipe(bs.stream());

export default scripts;
