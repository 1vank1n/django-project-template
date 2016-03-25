import gulp from 'gulp';
import plumber from 'gulp-plumber';
import changed from 'gulp-changed';
import imagemin from 'gulp-imagemin';
import notify from 'gulp-notify';

import { destImages } from './consts';

gulp.task('images', () => (
	gulp.src(['**/*.{png,jpg,gif}'], {
			cwd: 'frontend/images'
		})
		.pipe(plumber({errorHandler: notify.onError(
			(err) => ({
				title: 'Images',
				message: err.message
			})
		)}))
		.pipe(changed(destImages))
		.pipe(imagemin({
			optimizationLevel: 3,
			interlaced: true,
			progressive: true
		}))
		.pipe(gulp.dest(destImages))
));
