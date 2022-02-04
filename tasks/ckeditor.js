import { dest, src } from 'gulp';
import { distCkeditor, srcCkeditor } from './consts';

const ckeditor = () => src(`${srcCkeditor}/**`)
	.pipe(dest(`${distCkeditor}/`));

export default ckeditor;
