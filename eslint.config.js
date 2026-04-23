import js from '@eslint/js';
import globals from 'globals';

export default [
	js.configs.recommended,
	{
		files: ['frontend/**/*.js'],
		languageOptions: {
			ecmaVersion: 'latest',
			sourceType: 'module',
			globals: {
				...globals.browser,
			},
		},
		rules: {
			indent: ['error', 'tab'],
			'no-tabs': 'off',
			'no-unused-vars': 'warn',
		},
	},
];
