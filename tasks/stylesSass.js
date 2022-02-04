import { dest, src } from 'gulp';
import autoprefixer from 'gulp-autoprefixer';
import nano from 'gulp-cssnano';
import gcmq from 'gulp-group-css-media-queries';
import gulpif from 'gulp-if';
import sourcemaps from 'gulp-sourcemaps';
import { distStyles, isDevelopment, srcStyles } from './consts';
import { bs } from './default';

const sass = require('gulp-sass')(require('sass'));

const stylesSass = () => src(['base.scss'], {
	cwd: srcStyles,
})
	.pipe(gulpif(isDevelopment, sourcemaps.init()))
	.pipe(sass())
	.pipe(autoprefixer())
	.pipe(gulpif(!isDevelopment, gcmq()))
	.pipe(gulpif(!isDevelopment, nano()))
	.pipe(gulpif(isDevelopment, sourcemaps.write()))
	.pipe(dest(`${distStyles}/bootstrap/`))
	.pipe(bs.stream());

export default stylesSass;
