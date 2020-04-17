import del from 'del';
import { dist } from './consts';

const clean = () => del([
	`${dist}/**/*`,
	`!${dist}/ckeditor`,
	`!${dist}/ckeditor/**/*`,
]);

export default clean;
