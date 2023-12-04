import { rimraf } from 'rimraf';
import { dist } from './consts';

const clean = () => rimraf([
	`${dist}/**/*`,
	`!${dist}/ckeditor`,
	`!${dist}/ckeditor/**/*`,
]);

export default clean;
