import gulp from 'gulp';
import runSequence from 'run-sequence';
import watch from 'gulp-watch';

gulp.task('watch', () => {
	global.watch = true;

	watch('frontend/scripts/**/*', () => runSequence('scripts'));
	watch('frontend/styles/**/*', () => runSequence('styles'));
	watch('frontend/images/**/*', () => runSequence('images'));
	watch('frontend/fonts/**/*', () => runSequence('fonts'));
	watch('frontend/images/icons/**/*.svg', () => runSequence('icons'));

	gulp.start('scripts:watch');
});
