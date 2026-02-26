import { Transform } from 'stream';
import gulp from 'gulp';
import autoprefixer from 'gulp-autoprefixer';
import cleanCSS from 'gulp-clean-css';
import gulpif from 'gulp-if';
import Stylus from 'stylus';
import { distStyles, isDevelopment, srcStyles } from './consts.js';
import { bs } from './default.js';

function compileStylus(options = {}) {
	return new Transform({
		objectMode: true,
		transform(file, enc, cb) {
			if (file.isNull()) return cb(null, file);
			const compiler = Stylus(file.contents.toString())
				.set('filename', file.path)
				.set('paths', [srcStyles]);
			if (options['include css']) {
				compiler.set('include css', true);
			}
			try {
				file.contents = Buffer.from(compiler.render());
				file.extname = '.css';
				cb(null, file);
			} catch (err) {
				cb(err);
			}
		},
	});
}

const stylesStyl = () => gulp.src(['base.styl'], {
	cwd: srcStyles,
	sourcemaps: isDevelopment,
})
	.pipe(compileStylus({ 'include css': true }))
	.pipe(autoprefixer())
	.pipe(gulpif(!isDevelopment, cleanCSS()))
	.pipe(gulp.dest(distStyles, { sourcemaps: isDevelopment ? '.' : false }))
	.pipe(bs.stream());

export default stylesStyl;
