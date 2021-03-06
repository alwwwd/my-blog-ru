const {src , dest } = require('gulp');
const autoprefixer = require('gulp-autoprefixer');
const gcmq = require('gulp-group-css-media-queries');
const less = require('gulp-less');

const css_clear = require('gulp-clean-css');

const path = require('../config/path.js');

const css= () =>{
    return(src(path.src.scss))
        .pipe(less())
        .pipe(autoprefixer({
            overrideBrowserslist:["last 5 versions"],
            cascade:true
        }))
        .pipe(gcmq())
        .pipe(css_clear())
        .pipe(dest(path.dist.css))
}







module.exports = css;