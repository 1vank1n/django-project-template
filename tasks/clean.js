import { rimraf } from 'rimraf';
import { dist } from './consts';

const clean = () => rimraf(`${dist}/**/*`, {
	glob: true,
});

export default clean;
