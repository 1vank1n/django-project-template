import gulp from 'gulp';
import { srcFonts, distFonts } from './consts';

gulp.task('fonts', () =>
	gulp.src(`${srcFonts}/*`)
		.pipe(gulp.dest(distFonts)),
);
