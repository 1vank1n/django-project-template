import gulp from 'gulp';
import { srcImages, distImages } from './consts';

gulp.task('images', () =>
	gulp.src([`${srcImages}/*/**`, `!${srcImages}/*/icon*.svg`])
		.pipe(gulp.dest(distImages)),
);
