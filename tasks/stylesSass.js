import gulp from 'gulp';
import autoprefixer from 'gulp-autoprefixer';
import cleanCSS from 'gulp-clean-css';
import gulpif from 'gulp-if';
import gulpSass from 'gulp-sass';
import * as sassCompiler from 'sass';
import { distStyles, isDevelopment, srcStyles } from './consts.js';
import { bs } from './default.js';

const sass = gulpSass(sassCompiler);

const stylesSass = () => gulp.src(['base.scss'], {
	cwd: srcStyles,
	sourcemaps: isDevelopment,
})
	.pipe(sass())
	.pipe(autoprefixer())
	.pipe(gulpif(!isDevelopment, cleanCSS()))
	.pipe(gulp.dest(`${distStyles}/bootstrap/`, { sourcemaps: isDevelopment ? '.' : false }))
	.pipe(bs.stream());

export default stylesSass;
