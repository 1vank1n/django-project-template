import gulp from 'gulp';
import plumber from 'gulp-plumber';
import changed from 'gulp-changed';
import notify from 'gulp-notify';

import { destFonts } from './consts';

gulp.task('fonts', () => (
	gulp.src(['**/*.*'], {
			cwd: 'frontend/fonts'
		})
		.pipe(plumber({errorHandler: notify.onError(
			(err) => ({
				title: 'Fonts',
				message: err.message
			})
		)}))
		.pipe(changed(destFonts))
		.pipe(gulp.dest(destFonts))
));
