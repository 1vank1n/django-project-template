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
		css: {
			dest: '.',
			bust: false,
			sprite: '../images/icons.svg',
			layout: 'horizontal',
			prefix: '.',
			dimensions: true,
			render: {
				styl: {
					dest: 'svg-sprite.styl'
				}
			}
		}
	}
};

gulp.task('icons', () => (
	gulp.src(['**/*.svg'], {
			cwd: 'frontend/images/icons'
		})
		.pipe(plumber({errorHandler: notify.onError(
			(err) => ({
				title: 'Icons',
				message: err.message
			})
		)}))
		.pipe(svgSprite(svgSpriteConfig))
		.pipe(gulpif(/\.styl$/, gulp.dest('frontend/styles/helpers')))
		.pipe(gulpif(/\.svg$/, gulp.dest(destImages)))
));
