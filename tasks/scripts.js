import gulp from 'gulp';
import gulpif from 'gulp-if';
import sourcemaps from 'gulp-sourcemaps';
import babel from 'gulp-babel';
import concat from 'gulp-concat';
import plumber from 'gulp-plumber';
import notify from 'gulp-notify';

import { browserSync } from './default';
import { srcScripts, distScripts, isDevelopment } from './consts';

gulp.task('scripts', () => {
	gulp.src(`${srcScripts}/vendor/**`)
		.pipe(gulp.dest(`${distScripts}/vendor/`));

	gulp.src(`${srcScripts}/*.js`)
		.pipe(plumber({
			errorHandler: notify.onError(
				err => ({
					title: 'Html',
					message: err.message,
				}),
			),
		}))
		.pipe(gulpif(!isDevelopment, sourcemaps.init()))
		.pipe(babel({
			presets: ['es2015'],
		}))
		.pipe(concat('base.js'))
		.pipe(sourcemaps.write('.'))
		.pipe(gulp.dest(distScripts))
		.pipe(browserSync.stream());
});
