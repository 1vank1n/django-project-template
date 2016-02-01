import gulp from 'gulp';
import svgSymbols from 'gulp-svg-symbols';
import gulpif from 'gulp-if';
import rename from 'gulp-rename';
import plumber from 'gulp-plumber';
import errorHandler from 'gulp-plumber-error-handler';
import path from 'path';

gulp.task('icons', () => (
	gulp.src(['**/*.svg'], {
			cwd: 'frontend/images/icons'
		})
		.pipe(plumber({errorHandler: errorHandler('Error in \'icons\' task')}))
		.pipe(svgSymbols({
			title: false,
			id: 'icon_%f',
			className: '%f',
			templates: [
				path.join(__dirname, '../node_modules/stylus-svg-size-template/svg-size.styl'),
				'default-svg'
			]
		}))
		.pipe(gulpif(/\.styl$/, gulp.dest('frontend/styles/helpers')))
		.pipe(gulpif(/\.svg$/, rename('icon.svg')))
		.pipe(gulpif(/\.svg$/, gulp.dest('static/images')))
));
