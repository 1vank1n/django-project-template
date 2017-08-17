import gulp from 'gulp';
import svgSprite from 'gulp-svg-sprite';
import gulpif from 'gulp-if';
import plumber from 'gulp-plumber';
import notify from 'gulp-notify';

import { srcStyles, srcImages, distImages } from './consts';

const svgSpriteConfig = {
	shape: {
		id: {
			separator: '__',
		},
		spacing: {
			padding: 50,
		},
	},
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
					dest: 'svg-sprite.styl',
				},
			},
		},
	},
};

gulp.task('svg', () => (
	gulp.src(['**/icon*.svg'], {
		cwd: srcImages,
	})
		.pipe(plumber({
			errorHandler: notify.onError(
				err => ({
					title: 'Svg',
					message: err.message,
				}),
			),
		}))
		.pipe(svgSprite(svgSpriteConfig))
		.pipe(gulpif(/\.styl$/, gulp.dest(srcStyles)))
		.pipe(gulpif(/\.svg$/, gulp.dest(distImages)))
));
