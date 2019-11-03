// noinspection JSUnresolvedFunction
let gulp        = require( 'gulp' ),
    sass        = require( 'gulp-sass' ),
    concat      = require( 'gulp-concat' ),
    imagemin    = require( 'gulp-imagemin' ),
    rename      = require( 'gulp-rename' ),
    cleanCSS    = require( 'gulp-clean-css' ),
    babel       = require( 'gulp-babel' ),
    uglify      = require( 'gulp-uglify' ),
    imageResize = require( 'gulp-image-resize' ),
    // Configuration
    config      = {
        js                : {
            dest  : './static/',
            files : './static/source/js/*.js',
        },
        css               : {
            dest     : './static/',
            file     : './static/source/css/*.scss',
            partials : './static/source/css/**/*.scss',
        },
        backgrounds       : [ '', ],
        backgrounds_sizes : [ 768, 1024, 1200, 1920, ],
    };

/**
 * Concat and minify SASS files
 */
function sassTask () {

    return gulp
        .src( config.css.file )
        .pipe( sass() )
        .pipe( cleanCSS( { debug : true, }, function ( details ) {

            // noinspection JSUnresolvedVariable
            console.log( details.name + ': ' + details.stats.originalSize );
            // noinspection JSUnresolvedVariable
            console.log( details.name + ': ' + details.stats.minifiedSize );

        } ) )
        .pipe( rename( {

            suffix : '.min',

        } ) )
        .pipe( gulp.dest( config.css.dest ) );

}

/**
 * Concat, transpile and minify JavaScript files
 */
function transpileTask () {

    return gulp.src( config.js.files )
        .pipe( concat( 'scripts.babel.min.js' ) )
        .pipe( babel( {
            presets : [ '@babel/env', ],
        } ) )
        .pipe( uglify() )
        .pipe( gulp.dest( config.js.dest ) )

}

gulp.task( 'images', function () {

    return gulp.src( './static/source/img/**/*' )
        .pipe( imagemin( {
            interlaced          : true,
            progressive         : true,
            optimizationLevel   : 100,
            svgoPlugins         : [],
            verbose             : true,
        } ) )
        .pipe( gulp.dest( './static/img/' ) );

} );

// FIXME: This works...but it doesn't...
function resizeImages () {

    config.backgrounds_sizes.forEach( ( size ) => {

        return gulp.src( './static/source/img/backgrounds/*' )
            .pipe( imageResize( { width : size, imageMagick : true, quality : 0.74, } ) )
            .pipe( rename( ( path ) => {

            path.basename += `_@${ size }`;

        } ) )
            .pipe( gulp.dest( './static/img/backgrounds/' ) );

    } );

}
gulp.task( 'imageresize', gulp.series( resizeImages ) );

function watchTask () {

    gulp.watch(
        [ config.css.partials, config.js.files, ],
        gulp.parallel( sassTask, transpileTask )
    );

}

// Watch Files For Changes
gulp.task( 'serve', gulp.series( sassTask, transpileTask, watchTask ) );
