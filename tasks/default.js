import gulp from 'gulp';
import runSequence from 'run-sequence';
import browserSync from 'browser-sync';

browserSync.create();
module.exports.browserSync = browserSync;


gulp.task('browserSync', () => {
	browserSync.init({
		proxy: 'localhost:8000',
	});
});


gulp.task('default', () => (
	runSequence(
		'clean',
		'fonts',
		'styles',
		'scripts',
		'images',
		'svg',
		'browserSync',
		'watch',
	)
));
