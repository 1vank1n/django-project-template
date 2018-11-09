import del from 'del';
import { dist } from './consts';

const clean = () => del([`${dist}/**/*`]);

export default clean;
