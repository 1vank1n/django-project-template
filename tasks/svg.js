import gulp from 'gulp';
import gulpif from 'gulp-if';
import svgSprite from 'gulp-svg-sprite';
import { distImages, srcImages, srcStyles } from './consts.js';

const svgSpriteConfig = {
	shape: {
		id: {
			separator: '__',
		},
		spacing: {
			padding: 0,
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

const svg = () => gulp.src(['**/icon*.svg'], {
	cwd: srcImages,
})
	.pipe(svgSprite(svgSpriteConfig))
	.pipe(gulpif(/\.styl$/, gulp.dest(srcStyles)))
	.pipe(gulpif(/\.svg$/, gulp.dest(distImages)));

export default svg;
