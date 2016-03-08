import gulp from 'gulp';
import plumber from 'gulp-plumber';
import gutil from 'gulp-util';
import gulpif from 'gulp-if';
import rupture from 'rupture';
import stylus from 'gulp-stylus';
import autoprefixer from 'autoprefixer-stylus';
import gcmq from 'gulp-group-css-media-queries';
import nano from 'gulp-cssnano';
import sourcemaps from 'gulp-sourcemaps';
import errorHandler from 'gulp-plumber-error-handler';
import notify from 'gulp-notify';

import { destStyles, isDevelopment } from './consts.js'

gulp.task('styles', () => (
	gulp.src(['base.styl'], {
			cwd: 'frontend/styles'
		})
		.pipe(plumber({errorHandler: notify.onError(
			(err) => ({
				title: 'Styles',
				message: err.message
			})
		)}))
		.pipe(gulpif(isDevelopment, sourcemaps.init()))
		.pipe(stylus({
			use: [
				rupture(),
				autoprefixer()
			],
			'include css': true
		}))
		.pipe(gulpif(!isDevelopment, gcmq()))
		.pipe(gulpif(!isDevelopment, nano()))
		.pipe(gulpif(isDevelopment, sourcemaps.write()))
		.pipe(gulp.dest(destStyles))
));
