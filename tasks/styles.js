import gulp from 'gulp';
import plumber from 'gulp-plumber';
import gulpif from 'gulp-if';
import rupture from 'rupture';
import stylus from 'gulp-stylus';
import autoprefixer from 'autoprefixer-stylus';
import gcmq from 'gulp-group-css-media-queries';
import nano from 'gulp-cssnano';
import sourcemaps from 'gulp-sourcemaps';
import notify from 'gulp-notify';

import {destStyles, isDevelopment} from './consts.js';

gulp.task('styles', () => (
	gulp.src(['base.styl'], {
		cwd: 'frontend/styles'
	})
	.pipe(notify({
		message: 'Generated file: <%= file.relative %> @ <%= options.date %>',
		templateOptions: {
			date: new Date()
		}
	}))
	.pipe(plumber({errorHandler: notify.onError(
		err => ({
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
