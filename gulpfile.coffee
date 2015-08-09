gulp         = require 'gulp'
plumber      = require 'gulp-plumber'
gutil        = require 'gulp-util'
gulpif       = require 'gulp-if'
changed      = require 'gulp-changed'
imagemin     = require 'gulp-imagemin'
rupture      = require 'rupture'
stylus       = require 'gulp-stylus'
autoprefixer = require 'gulp-autoprefixer'
cmq          = require 'gulp-combine-media-queries'
minifyCss    = require 'gulp-minify-css'
csscomb      = require 'gulp-csscomb'
runSequence  = require 'run-sequence'
uglify       = require 'gulp-uglify'
concat       = require 'gulp-concat'

# paths
srcStyles = 'frontend/styles/base.css'
distStyles = 'static/styles/'
distScripts = 'static/scripts/'

# tasks
gulp.task 'styles', ->
    gulp.src ['base.styl'], cwd: 'frontend/styles'
        .pipe plumber()
        .pipe stylus
            errors: true,
            use: rupture()
            sourcemap: if gutil.env.debug then {comment: false, inline: true} else false
        .pipe autoprefixer()
        .pipe gulpif !gutil.env.debug, cmq()
        .pipe gulpif !gutil.env.debug, minifyCss()
        .pipe gulpif gutil.env.csscomb, csscomb()
        .pipe gulp.dest distStyles

gulp.task 'scripts', ->
    gulp.src ['*.js'], cwd: 'frontend/scripts'
        .pipe uglify()
        .pipe concat 'scripts.js'
        .pipe gulp.dest distScripts

gulp.task 'imagemin', ->
    gulp.src [
            '**/*.{png,jpg,gif}'
        ],
            cwd: 'frontend/images'
        .pipe plumber()
        .pipe changed 'static/images/tmp'
        .pipe imagemin
            optimizationLevel: 3
            interlaced: true
            progressive: true
        .pipe gulp.dest 'static/images'

gulp.task 'watch', ->
    global.watch = true
    gulp.watch 'frontend/styles/**/*', ['styles']
    gulp.watch 'frontend/scripts/**/*', ['scripts']
    gulp.watch 'frontend/images/**/*', ['imagemin']

gulp.task 'default', ->
    runSequence(
        'styles'
        'scripts'
        'imagemin'
        'watch'
    )
