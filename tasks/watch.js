import { watch } from 'gulp';
import {
	srcFonts, srcImages, srcScripts, srcStyles, srcTemplates
} from './consts';
import { bs } from './default';
import fonts from './fonts';
import images from './images';
import scripts from './scripts';
import scriptsVendor from './scriptsVendor';
import stylesSass from './stylesSass';
import stylesStyl from './stylesStyl';
import svg from './svg';

const html = (cb) => {
	bs.reload();
	cb();
};

const watcher = () => {
	global.watch = true;

	watch(`${srcFonts}/**`, fonts);
	watch(`${srcImages}/**`, images);
	watch(`${srcImages}/**/icon*.svg`, svg);
	watch(`${srcStyles}/**/*`, stylesStyl);
	watch(`${srcStyles}/**/*`, stylesSass);
	watch(`${srcScripts}/**/*`, scriptsVendor);
	watch(`${srcScripts}/**/*`, scripts);
	watch(`${srcTemplates}/**/*`, html);
	watch('applications/**/templates/**/*', html);
};

export default watcher;
