import gulp from 'gulp';
import del from 'del';
import { dist } from './consts';


gulp.task('clean', () =>
	del([
		`${dist}/**/*`,
	]),
);
