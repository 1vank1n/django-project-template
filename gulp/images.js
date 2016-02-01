import gulp from 'gulp';
import plumber from 'gulp-plumber';
import changed from 'gulp-changed';
import imagemin from 'gulp-imagemin';

gulp.task('images', () => (
	gulp.src(['**/*.{png,jpg,gif}'], {
			cwd: 'frontend/images'
		})
		.pipe(plumber())
		.pipe(changed('static/images/tmp'))
		.pipe(imagemin({
			optimizationLevel: 3,
			interlaced: true,
			progressive: true
		}))
		.pipe(gulp.dest('static/images'))
));
