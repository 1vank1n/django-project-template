import { resolve } from 'node:path';
import { defineConfig } from 'vite';

export default defineConfig({
	root: resolve(import.meta.dirname, 'frontend'),
	base: '/static/vite/',
	build: {
		outDir: resolve(import.meta.dirname, 'static/vite'),
		emptyOutDir: true,
		manifest: 'manifest.json',
		rollupOptions: {
			input: {
				base: resolve(import.meta.dirname, 'frontend/scripts/base.js'),
				styles: resolve(import.meta.dirname, 'frontend/styles/base.scss'),
			},
		},
	},
	server: {
		host: '0.0.0.0',
		port: 5173,
		strictPort: true,
		origin: 'http://localhost:5173',
	},
});
