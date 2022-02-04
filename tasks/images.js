import { dest, src } from 'gulp';
import { distImages, srcImages } from './consts';

const images = () => src([`${srcImages}/**`, `!${srcImages}/*/icon*.svg`])
	.pipe(dest(distImages));

export default images;
