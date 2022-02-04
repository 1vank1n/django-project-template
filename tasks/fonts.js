import { dest, src } from 'gulp';
import { distFonts, srcFonts } from './consts';

const fonts = () => src(`${srcFonts}/*`)
	.pipe(dest(distFonts));

export default fonts;
