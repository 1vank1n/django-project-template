import { rimraf } from 'rimraf';
import { dist } from './consts.js';

const clean = () => rimraf(`${dist}/**/*`, {
	glob: true,
});

export default clean;
