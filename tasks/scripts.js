import { dest, src } from 'gulp';
import babel from 'gulp-babel';
import concat from 'gulp-concat';
import gulpif from 'gulp-if';
import sourcemaps from 'gulp-sourcemaps';
import { distScripts, isDevelopment, srcScripts } from './consts';
import { bs } from './default';

const scripts = () => src(`${srcScripts}/*.js`)
	.pipe(gulpif(isDevelopment, sourcemaps.init()))
	.pipe(babel())
	.pipe(concat('base.js'))
	.pipe(sourcemaps.write('.'))
	.pipe(dest(distScripts))
	.pipe(bs.stream());

export default scripts;
