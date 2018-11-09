import { src, dest } from 'gulp';
import { srcFonts, distFonts } from './consts';

const fonts = () => src(`${srcFonts}/*`)
	.pipe(dest(distFonts));

export default fonts;
