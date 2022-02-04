import { dest, src } from 'gulp';
import { distScripts, srcScripts } from './consts';

const scriptsVendor = () => src(`${srcScripts}/vendor/**`)
	.pipe(dest(`${distScripts}/vendor/`));

export default scriptsVendor;
