import browserSync from 'browser-sync';

export const bs = browserSync.create();

const bsTask = () => bs.init({
	proxy: 'localhost:8000',
	browser: 'google chrome canary',
});

export default bsTask;
