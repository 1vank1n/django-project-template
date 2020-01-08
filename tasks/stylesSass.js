import { src, dest } from 'gulp';
import plumber from 'gulp-plumber';
import gulpif from 'gulp-if';
import gcmq from 'gulp-group-css-media-queries';
import nano from 'gulp-cssnano';
import sourcemaps from 'gulp-sourcemaps';
import sass from 'gulp-sass';
import notify from 'gulp-notify';
import { bs } from './default';
import { srcStyles, distStyles, isDevelopment } from './consts';

sass.compiler = require('node-sass');

const stylesSass = () => src(['base.scss'], {
	cwd: srcStyles,
})
	.pipe(notify({
		message: 'Generated file: <%= file.relative %> @ <%= options.date %>',
		templateOptions: {
			date: new Date(),
		},
	}))
	.pipe(plumber({
		errorHandler: notify.onError(
			(err) => ({
				title: 'Sass',
				message: err.message,
			}),
		),
	}))
	.pipe(gulpif(isDevelopment, sourcemaps.init()))
	.pipe(sass())
	.pipe(gulpif(!isDevelopment, gcmq()))
	.pipe(gulpif(!isDevelopment, nano()))
	.pipe(gulpif(isDevelopment, sourcemaps.write()))
	.pipe(dest(`${distStyles}/bootstrap4/`))
	.pipe(bs.stream());

export default stylesSass;
