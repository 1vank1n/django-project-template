module.exports = {
	parser: '@babel/eslint-parser',
	extends: 'airbnb-base',
	rules: {
		indent: ['error', 'tab'],
		'no-tabs': 0,
	},
	env: {
		browser: true,
		jquery: true,
	},
	globals: {
		flexibility: true,
		bootstrap: true,
	},
};
