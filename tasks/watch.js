import { watch } from 'gulp';
import {
	srcFonts, srcImages, srcStyles, srcScripts, srcTemplates,
} from './consts';
import fonts from './fonts';
import images from './images';
import svg from './svg';
import scriptsVendor from './scriptsVendor';
import scripts from './scripts';
import styles from './styles';
import { bs } from './default';

const html = (cb) => {
	bs.reload();
	cb();
};

const watcher = () => {
	global.watch = true;

	watch(`${srcFonts}/**`, fonts);
	watch(`${srcImages}/**`, images);
	watch(`${srcImages}/**/icon*.svg`, svg);
	watch(`${srcStyles}/**/*`, styles);
	watch(`${srcScripts}/**/*`, scriptsVendor);
	watch(`${srcScripts}/**/*`, scripts);
	watch(`${srcTemplates}/**/*`, html);
	watch('applications/**/templates/**/*', html);
};

export default watcher;
