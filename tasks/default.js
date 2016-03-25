import gulp from 'gulp';
import runSequence from 'run-sequence';

gulp.task('styles:dependencies', () => (
	runSequence (
		'icons',
		'styles'
	)
));

gulp.task('default', () => (
	runSequence (
		'styles:dependencies',
		'images',
		'fonts',
		'watch'
	)
));

gulp.task('build', () => (
	runSequence (
		'styles:dependencies',
		'scripts',
		'images',
		'fonts'
	)
));
