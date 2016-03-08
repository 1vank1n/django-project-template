import path from 'path';
import gulp from 'gulp';
import gutil from 'gulp-util';
import webpack from 'webpack';
import webpackStream from 'webpack-stream';
import stylish from 'eslint/lib/formatters/stylish';
import notifier from 'node-notifier';
import plumber from 'gulp-plumber';
import errorHandler from 'gulp-plumber-error-handler';
import statsLogger from 'webpack-stats-logger';
import notify from 'gulp-notify';

import { destScripts, isDevelopment } from './consts.js'

function runWebpack(watch = false) {
	const webpackConfig = {
		watch,
		bail: false,
		profile: true,
		output: {
			filename: 'base.js',
			pathinfo: false
		},
		devtool: (!isDevelopment) ? '#source-map' : 'eval',
		debug: true,
		resolve: {
			modulesDirectories: [
				'node_modules'
			],
			extensions: ['.js', '']
		},
		module: {
			preLoaders: [
				{
					test: /\.js$/,
					loader: 'source-map-loader'
				}
			],
			loaders: [
				{
					test: /\.js$/,
					loader: 'babel',
					exclude: /node_modules/
				},
				{
					test: /\.json$/,
					loader: 'json'
				},
				{
					test: /\.js$/,
					loader: 'eslint-loader',
					exclude: /node_modules/
				}
			]
		},
		plugins: isDevelopment ? [] : [
			new webpack.optimize.DedupePlugin(),
			new webpack.optimize.UglifyJsPlugin({
				compress: {
					warnings: false
				},
				output: {
					comments: false
				}
			})
		],
		eslint: {
			configFile: path.join(__dirname, '../.eslintrc'),
			emitError: true,
			emitWarning: true
		},
		externals: {
			jquery: "$"
		},
	};

	return gulp
		.src('frontend/scripts/*')
		.pipe(plumber({errorHandler: notify.onError(
			(err) => ({
				title: 'Scripts',
				message: err.message
			})
		)}))
		.pipe(webpackStream(webpackConfig, null, statsLogger))
		.pipe(gulp.dest(destScripts));
}

gulp.task('scripts', () => {
	return runWebpack(false);
});

gulp.task('scripts:watch', () => {
	return runWebpack(true);
});
