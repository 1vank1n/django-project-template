import gulp from 'gulp';
import svgSprite from 'gulp-svg-sprite';
import gulpif from 'gulp-if';
import rename from 'gulp-rename';
import plumber from 'gulp-plumber';
import errorHandler from 'gulp-plumber-error-handler';
import notify from 'gulp-notify';

import { destImages } from './consts';

const svgSpriteConfig = {
	mode: {
		symbol: {
			render: {
				styl: {dest: 'svg-size.styl'}
			}
		}
	}
};

gulp.task('icons', () => (
	gulp.src(['**/*.svg'], {
			cwd: 'frontend/images/icons'
		})
		.pipe(plumber({errorHandler: errorHandler('Error in \'icons\' task')}))
		.pipe(svgSprite(svgSpriteConfig))
		.pipe(gulpif(/\.svg$/, rename('icon.svg')))
		.pipe(gulpif(/\.styl$/, rename('svg-size.styl')))
		.pipe(gulpif(/\.styl$/, gulp.dest('frontend/styles/helpers')))
		.pipe(gulpif(/\.svg$/, gulp.dest(destImages)))
));
