import { Transform } from 'stream';
import { dest, src } from 'gulp';
import autoprefixer from 'gulp-autoprefixer';
import cleanCSS from 'gulp-clean-css';
import gcmq from 'gulp-group-css-media-queries';
import gulpif from 'gulp-if';
import sourcemaps from 'gulp-sourcemaps';
import Stylus from 'stylus';
import { distStyles, isDevelopment, srcStyles } from './consts';
import { bs } from './default';

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

const stylesStyl = () => src(['base.styl'], {
	cwd: srcStyles,
})
	.pipe(gulpif(isDevelopment, sourcemaps.init()))
	.pipe(compileStylus({ 'include css': true }))
	.pipe(autoprefixer())
	.pipe(gulpif(!isDevelopment, gcmq()))
	.pipe(gulpif(!isDevelopment, cleanCSS()))
	.pipe(gulpif(isDevelopment, sourcemaps.write()))
	.pipe(dest(distStyles))
	.pipe(bs.stream());

export default stylesStyl;
