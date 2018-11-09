import { src, dest } from 'gulp';
import { srcScripts, distScripts } from './consts';

const scriptsVendor = () => src(`${srcScripts}/vendor/**`)
	.pipe(dest(`${distScripts}/vendor/`));

export default scriptsVendor;
