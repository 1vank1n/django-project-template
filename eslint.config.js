import globals from 'globals';

export default [
	{
		files: ['frontend/**/*.js'],
		languageOptions: {
			ecmaVersion: 'latest',
			sourceType: 'module',
			globals: {
				...globals.browser,
				...globals.jquery,
				flexibility: 'readonly',
				bootstrap: 'readonly',
			},
		},
		rules: {
			indent: ['error', 'tab'],
			'no-tabs': 'off',
			'no-unused-vars': 'warn',
		},
	},
];
