import gulp from 'gulp';
import runSequence from 'run-sequence';
import watch from 'gulp-watch';
import { browserSync } from './default';
import { srcFonts, srcImages, srcStyles, srcScripts, srcTemplates } from './consts';

gulp.task('watch', () => {
	global.watch = true;

	watch(`${srcFonts}/**/*`, () => runSequence('fonts'));
	watch(`${srcImages}/**/*`, () => runSequence('images'));
	watch(`${srcImages}/**/icon*.svg`, () => runSequence('svg'));
	watch(`${srcStyles}/**/*`, () => runSequence('styles'));
	watch(`${srcScripts}/**/*`, () => runSequence('scripts'));
	watch(`${srcTemplates}/**/*`, () => browserSync.reload());
});
