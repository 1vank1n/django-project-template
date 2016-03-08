import gulp from 'gulp';
import plumber from 'gulp-plumber';
import changed from 'gulp-changed';

import { destFonts } from './consts';

gulp.task('fonts', () => (
	gulp.src(['**/*.*'], {
			cwd: 'frontend/fonts'
		})
		.pipe(plumber())
		.pipe(changed(destFonts))
		.pipe(gulp.dest(destFonts))
));
