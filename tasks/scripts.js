import { src, dest } from 'gulp';
import gulpif from 'gulp-if';
import sourcemaps from 'gulp-sourcemaps';
import babel from 'gulp-babel';
import concat from 'gulp-concat';
import plumber from 'gulp-plumber';
import notify from 'gulp-notify';

import { bs } from './default';
import { srcScripts, distScripts, isDevelopment } from './consts';

const scripts = () => src(`${srcScripts}/*.js`)
	.pipe(plumber({
		errorHandler: notify.onError(
			(err) => ({
				title: 'Script',
				message: err.message,
			}),
		),
	}))
	.pipe(gulpif(!isDevelopment, sourcemaps.init()))
	.pipe(babel())
	.pipe(concat('base.js'))
	.pipe(sourcemaps.write('.'))
	.pipe(dest(distScripts))
	.pipe(bs.stream());

export default scripts;
