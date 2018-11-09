import { src, dest } from 'gulp';
import { srcImages, distImages } from './consts';

const images = () => src([`${srcImages}/**`, `!${srcImages}/*/icon*.svg`])
	.pipe(dest(distImages));

export default images;
