import autoprefixer from 'autoprefixer-stylus';
import { dest, src } from 'gulp';
import cleanCSS from 'gulp-clean-css';
import gcmq from 'gulp-group-css-media-queries';
import gulpif from 'gulp-if';
import sourcemaps from 'gulp-sourcemaps';
import stylus from 'gulp-stylus';
import { distStyles, isDevelopment, srcStyles } from './consts';
import { bs } from './default';

const stylesStyl = () => src(['base.styl'], {
	cwd: srcStyles,
})
	.pipe(gulpif(isDevelopment, sourcemaps.init()))
	.pipe(stylus({
		use: [
			autoprefixer(),
		],
		'include css': true,
	}))
	.pipe(gulpif(!isDevelopment, gcmq()))
	.pipe(gulpif(!isDevelopment, cleanCSS()))
	.pipe(gulpif(isDevelopment, sourcemaps.write()))
	.pipe(dest(distStyles))
	.pipe(bs.stream());

export default stylesStyl;
